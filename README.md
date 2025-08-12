# Voice ChatBot 🤖

This is a simple Voice-to-Text AI Chatbot built in Python.  
It listens to your voice, recognizes the speech, generates a response using an AI model, and speaks it back to you.

---

## Features :
- Voice Recognition —> Listens and converts your speech to text.
- AI Responses —> Answers your questions intelligently.
- Text-to-Speech —> Speaks the AI's answer out loud.
- Date & Time —> Can tell you the current date and time.
- Conversation logging to chat_log.txt.
- Audio recordings of user input saved to recordings/ folder.
- Exit command with keywords: "exit", "quit", or "bye".

---

## Requirements :
Python 3.7+
Packages:
torch
transformers
speechrecognition
gtts
playsound
pyaudio (for microphone input)

---

## How to Run ?
1. Clone or download this project to your computer.
2. Navigate to the project folder in your terminal.
3. Activate your Python environment (if using one).
4. Run the chatbot:
   ```bash
   python chatbot.py

---

## Example Usge :


---

## Troubleshooting :
If the chatbot does not understand your speech, try speaking clearly or reducing background noise.
You might see warnings about tokenizer parallelism; these do not affect functionality.
If audio playback does not work, ensure playsound is installed and configured properly on your system.
Notes
The AI replies are generated based on the facebook/blenderbot-400M-distill model, which is designed for conversational tasks.
The chatbot currently handles each input independently without a long conversation history to keep responses relevant and avoid repetition.

--- 

## Author :
Made By: Sura Abdullah Alkhuzaim



