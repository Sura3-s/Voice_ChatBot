import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline
import speech_recognition as sr
from gtts import gTTS
import playsound
import datetime
import os

# Load conversation model BlenderBot (smaller, faster, designed for chatting)
print("Loading AI model...")
model_id = "facebook/blenderbot-400M-distill"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSeq2SeqLM.from_pretrained(model_id)
pipe = pipeline(
    "text2text-generation",
    model=model,
    tokenizer=tokenizer,
    device=0 if torch.cuda.is_available() else -1,
    max_length=100,
    do_sample=True,
    temperature=0.7
)
print("AI model is ready.")

# File to store chat logs and folder to store audio recordings
log_file = "chat_log.txt"
audio_folder = "recordings"
os.makedirs(audio_folder, exist_ok=True)

# Listen to microphone input and convert speech to text
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... Speak now.")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)  # Wait until silence automatically

    audio_filename = os.path.join(audio_folder, datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".wav")
    with open(audio_filename, "wb") as f:
        f.write(audio.get_wav_data())

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio, language="en-US")
        print("You said:", text)
        return text.strip()
    except sr.UnknownValueError:
        print("Could not understand the audio.")
        return None
    except sr.RequestError as e:
        print("Speech recognition error:", e)
        return None

# Convert text to speech using gTTS
def speak(text):
    print("AI says:", text)
    tts = gTTS(text=text, lang='en')
    filename = "temp.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

# Generate AI response (with some built-in commands)
def get_ai_response(prompt):
    prompt_lower = prompt.lower()
    if "time" in prompt_lower:
        return datetime.datetime.now().strftime("The current time is %I:%M %p.")
    elif "date" in prompt_lower or "day" in prompt_lower:
        return datetime.datetime.now().strftime("Today is %A, %B %d, %Y.")
    elif "how are you" in prompt_lower:
        return "I'm doing well, thank you! How can I help you today?"

    result = pipe(prompt)[0]['generated_text']
    return result.strip()

# Main program loop
def main():
    with open(log_file, "w", encoding="utf-8") as f:
        f.write("Chat Log\n" + "="*30 + "\n")

    while True:
        user_input = listen()

        if not user_input:
            speak("Sorry, I didn't catch that. Please try again.")
            continue

        if len(user_input.split()) < 2:
            speak("Could you please say a bit more?")
            continue

        if any(word in user_input.lower() for word in ["exit", "quit", "bye"]):
            speak("Goodbye!")
            break

        try:
            response = get_ai_response(user_input)
        except Exception as e:
            print("Error generating response:", e)
            response = "Sorry, I encountered an error."

        speak(response)

        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"You: {user_input}\nAI: {response}\n\n")

if __name__ == "__main__":
    main()
