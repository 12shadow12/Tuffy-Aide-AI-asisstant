import pyttsx3
import speech_recognition as sr
import weather
import greetings


def say(audio: str) -> None:
    
    tts = pyttsx3.init()
    voices = tts.getProperty('voices')

    tts.setProperty('voice', voices[1].id)
    tts.setProperty('rate', 140)

    tts.say(audio)
    tts.runAndWait()


def command() -> str:

    recognizer = sr.Recognizer()
    command = None
    
    with sr.Microphone() as source:

        recognizer.pause_threshold = .6
        audio = recognizer.listen(source, 5)

        try:
            command = recognizer.recognize_google(audio, language='en')
            
        except:
            say("I'm sorry, I could not understand.")
        
        return command


def greet():
    say(greetings.greet)


def listenForCommand():
    #greet()
    say("How can i help you?")

    while(True):

        c = command().lower()
        print(c)
        if "weather" in c:
            city = c[-1]
            print(c)
            print(city)
            # w = weather.Weather().getWeather(city)
            # desc = w["desc"]
            # temp = w["temp"]
            # high = w["high"]
            # low = w["low"]

            # say(f'The current weather in {city} is {desc} and {temp} degrees with a high of {high} and a low of {low}.')


listenForCommand()