import pyttsx3
import speech_recognition as sr
import weather
import jokes


def say(audio: str) -> None:
    
    tts = pyttsx3.init()
    voices = tts.getProperty('voices')

    tts.setProperty('voice', voices[1].id)
    tts.setProperty('rate', 85)

    tts.say(audio)
    tts.runAndWait()


def listenForCommand() -> str:

    recognizer = sr.Recognizer()
    command = None
    
    with sr.Microphone() as source:

        recognizer.pause_threshold = .6
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio, language='en')
            
        except:
            say("I'm sorry, I could not understand.")
        
        return command
