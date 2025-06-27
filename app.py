from flask import Flask, request, jsonify, render_template
import os
import json
import speech_recognition as sr
import sounddevice as sd
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load user profile JSON
with open("profile.json", "r", encoding="utf-8") as f:
    user_data = json.load(f)

# Initialize Flask app and Gemini model
app = Flask(__name__, static_folder="static", template_folder="templates")
recognizer = sr.Recognizer()
model = genai.GenerativeModel("models/gemini-2.0-flash")

# Record audio from mic using sounddevice
def record_audio(duration=5, fs=16000):
    print("🎤 Recording...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    return sr.AudioData(audio.tobytes(), fs, 2)

# Prompt builder
def build_prompt(question):
    return f"""
Hey, I’m James. Here’s some information about me:
{json.dumps(user_data, indent=2)}

If someone asks me a question, please answer it like I'm personally speaking to them — using "I", "me", and "my" — as if we’re having a real conversation. Don’t say things like “based on the data” or “according to the profile.”

Here’s the question I was asked:
{question}

Please give a clear and friendly response, like I’m talking to them directly.
"""

# Homepage route
@app.route("/")
def index():
    return render_template("index.html")

# POST route for voice questions
@app.route("/listen", methods=["POST"])
def listen():
    try:
        audio = record_audio()
        question = recognizer.recognize_google(audio)

        prompt = build_prompt(question)
        response = model.generate_content(prompt)
        answer = response.text.strip()

        return jsonify({
            "question": question,
            "answer": answer
        })

    except sr.UnknownValueError:
        return jsonify({"error": "Could not understand audio"}), 400
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

# POST route for typed questions
@app.route("/ask", methods=["POST"])
def ask():
    try:
        data = request.get_json()
        question = data.get("question", "")

        if not question.strip():
            return jsonify({"error": "Question cannot be empty"}), 400

        prompt = build_prompt(question)
        response = model.generate_content(prompt)
        answer = response.text.strip()

        return jsonify({
            "question": question,
            "answer": answer
        })

    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

# Run the server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
