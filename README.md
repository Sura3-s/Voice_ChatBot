# Voice ChatBot 🤖

## Overview :
This is a voice-activated AI chatbot built in Python that uses a pretrained conversational language model (facebook/blenderbot-400M-distill) to generate natural language responses.
It listens to your speech via microphone, converts it to text, generates AI replies, and speaks back the responses. The chatbot supports basic commands like asking the current time and date.

---

## Features :
Speech recognition with microphone input using speech_recognition.
Natural language generation with Hugging Face's transformers BlenderBot model.
Text-to-speech using Google Text-to-Speech (gTTS) and playsound.
Conversation logging to chat_log.txt.
Audio recordings of user input saved to recordings/ folder.
Handles simple commands (time, date, greetings).
Exit command with keywords: "exit", "quit", or "bye".

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

You can install the Python dependencies with:
pip install torch transformers speechrecognition gtts playsound pyaudio
Note: Installing pyaudio might require additional system dependencies depending on your OS.
Usage
Activate your Python environment if using virtualenv.
Run the chatbot script:
python chatbot.py
Speak into your microphone when prompted.
To exit the chatbot, say "exit", "quit", or "bye".

---

## Example Questions to Ask :
- What is your name?
- Tell me a joke.
- How can I improve my English?
- What is AI?
- What day is today?
- What time is it now?

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



