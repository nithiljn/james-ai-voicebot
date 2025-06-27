# 🎙️ James AI Voice Assistant

A voice-based personal portfolio assistant powered by **Gemini AI** for question answering and **ResponsiveVoice.js** for speech output. Ask anything about James — education, projects, skills, and more — and get answers in both text and voice!

---

## 🚀 Features

- 🎤 Voice input using microphone
- 🤖 Gemini AI for intelligent responses
- 🗣️ Text-to-Speech with ResponsiveVoice (auto playback)
- 🧑 Personalized with James' profile (from JSON)
- 🌐 Flask-based web UI with dual chat layout
- 💬 Optional text input button

---

## 📁 Project Structure

```
📦 James-AI-VoiceBot
├── app.py                # Flask backend
├── templates/
│   └── index.html       # Frontend (UI)
├── static/
│   └── response.mp3     # Output voice file (for testing fallback)
├── profile.json         # James' personal info (used for prompting)
├── requirements.txt     # Python dependencies
├── .env                 # Secret keys (Gemini API etc.)
├── render.yaml          # Deployment config (Render)
└── README.md            # This file
```

---

## 🛠️ Tech Stack

- 💬 **Gemini 2.0 Flash** (Google Generative AI)
- 🎙️ **SpeechRecognition** + sounddevice
- 🔊 **ResponsiveVoice.js** (Text-to-Speech)
- 🌐 **Flask** + HTML/CSS (Frontend)
- 🧠 **Python 3.10+** (Recommend 3.10.x for compatibility)

---

## 🧪 Local Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/james-ai-voicebot.git
   cd james-ai-voicebot
   ```

2. **Create and activate virtual environment:**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # for Windows
   # or
   source venv/bin/activate  # for macOS/Linux
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add your .env file:**
   ```ini
   GEMINI_API_KEY=your_google_gemini_api_key
   ```

5. **Run the app:**
   ```bash
   python app.py
   ```

6. **Open your browser and navigate to:**
   ```
   http://localhost:5000
   ```

---

## 🌍 Deployment (Render)

This project supports Render.com auto-deployment via `render.yaml`.

1. Push code to GitHub
2. Create Render Web Service → Choose GitHub repo
3. Add environment variable:
   ```
   GEMINI_API_KEY=your_actual_api_key
   ```
4. Click Deploy

---

## 📋 Requirements

- Python 3.10+
- Google Gemini API Key
- Modern web browser with microphone support
- Internet connection for API calls

---

## 🎯 Usage

1. **Voice Input:** Click the microphone button and speak your question
2. **Text Input:** Type your question in the input field
3. **Get Response:** Receive both text and voice responses about James
4. **Ask Anything:** Education, projects, skills, experience, or general questions

---

## 🙋 About Me

Hi! I'm **James Nithil V**, a B.Tech (AI & Data Science) graduate passionate about building AI-driven systems. This is one of my portfolio projects to showcase AI + voice tech integration.

- 🔗 [LinkedIn](https://www.linkedin.com/in/jamesnithil-v/)
- 💻 [GitHub](https://github.com/nithiljn)

---

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🔧 Troubleshooting

- **Microphone not working:** Ensure browser permissions are granted
- **API errors:** Check your Gemini API key in the .env file
- **Voice not playing:** Ensure ResponsiveVoice.js is loaded and browser supports audio

---

## 🚀 Future Enhancements

- [ ] Multiple language support
- [ ] Voice customization options
- [ ] Chat history persistence
- [ ] Mobile app version
- [ ] Integration with more AI models

---

**Made with ❤️ by James Nithil V**