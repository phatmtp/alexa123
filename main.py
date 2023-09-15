import speech_recognition as sr
import pyttsx3

# Initialize the speech recognition and text-to-speech engines
r = sr.Recognizer()
engine = pyttsx3.init()

# Define voice commands and responses
commands = {
    'what can you do': 'Hello! How can I assist you?',
    'what is your name': 'My name is Assistant.',
    'how is the weather': 'Sorry, I am not connected to the internet.'
}

# Listen for user command
with sr.Microphone() as source:
    print("Listening...")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    
    # Convert speech to text
    text = r.recognize_google(audio)
    print("User Command:", text)
    
    # Process user command and generate response
    for command, response in commands.items():
        if command in text.lower():
            print("Assistant:", response)
            engine.say(response)
            engine.runAndWait()
            break
    else:
        print("Assistant: Sorry, I didn't understand.")
