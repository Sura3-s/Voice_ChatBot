# Voice ChatBot 🤖
This is a simple Voice-to-Text AI Chatbot built in Python.  
It listens to your voice, recognizes the speech, generates a response using an AI model, and speaks it back to you.

---

## Features :
- Voice Recognition → Listens and converts your speech to text.
- AI Responses → Answers your questions intelligently.
- Text-to-Speech → Speaks the AI's answer out loud.
- Date & Time → Can tell you the current date and time.
- Conversation Logging → Saves chat history to chat_log.txt.
- Audio Recording → Saves user input audio to recordings/ folder.
- Exit Command → Keywords: "exit", "quit", or "bye".

---

## Requirements :
- Python 3.7+

### Install required packages:
```bash
pip install torch torchvision torchaudio
pip install transformers
pip install SpeechRecognition
pip install gtts
pip install playsound
pip install pyaudio
```
---

## How to Run ?
1. Clone or download this project to your computer.
2. Open a terminal and navigate to the project folder.
3. (Optional) Activate your Python virtual environment.
4. Run the chatbot:
   ```bash
   python chatbot.py

---

## Example Usge :
 • User: “Hello, how are you?”
 • Bot: “I’m doing well, thank you! How can I help you today?”
 • User: “What’s the date today?”
 • Bot: “Today is Tuesday, August 12, 2025.”
 • User: “Exit”
 • Bot: “Goodbye!”

---

## Notes :
 - Make sure your microphone is working.
 - Requires an internet connection to run the AI model.
 - If the AI doesn’t hear you properly, try speaking clearly and loudly.

--- 

## Author :
Made By: Sura Abdullah Alkhuzaim
