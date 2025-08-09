# Voice_ChatBot 🤖


A voice-controlled AI assistant using:
- HuggingFace Falcon LLM
- SpeechRecognition for speech-to-text
- gTTS for text-to-speech
- Python

---

## Features:
- Understands English speech (configurable for Arabic)
- Speaks English responses with natural voice
- Knows built-in commands (time, date, greetings)
- Can answer any question using an AI model
- Remembers conversation context
- Saves all chats in a log file
- Saves audio recordings

---

## Requirements:
- Python 3.9+
- Microphone
- Internet connection

---

## Installation:

1. Clone or download this project.
2. Install dependencies:
```bash
pip install torch torchvision torchaudio
pip install transformers
pip install SpeechRecognition
pip install gTTS
pip install playsound==1.2.2
pip install pyaudio
