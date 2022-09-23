#!/usr/bin/env python3
import pyttsx3
import speech_recognition as sr
import weather
import greetings
from datetime import datetime
import time
#import jokes


def say(audio: str) -> None:
    
    tts = pyttsx3.init()
    voices = tts.getProperty('voices')

    tts.setProperty('voice', voices[1].id)
    tts.setProperty('rate', 175)

    tts.say(audio)
    tts.runAndWait()


def command() -> str:

    recognizer = sr.Recognizer()
    command = None
    
    with sr.Microphone() as source:

        recognizer.pause_threshold = .6

        try:
            audio = recognizer.listen(source, 5)
        except sr.WaitTimeoutError:
            pass
            return command

        try:
            command = recognizer.recognize_google(audio, language='en')
        except:
            say("I'm sorry, I could not understand. How may I help you?")
            return None
        
        return command


def greet() -> None:
    say(greetings.greet)


def listen():

    c = command()
    print(c)
    if c:
        c = c.lower()
        if "tuffy" in c or "toffee" in c or "taffy" in c:
            respondToCommand()


def respondToCommand() -> None:
    greet()
    say("How can I help you?")

    while True:

        c = command()
        if c:
            c = c.lower().split(" ")
            if "weather" in c:
                city = c[-1]
                w = weather.Weather().getWeather(city)
                desc = w["desc"]
                temp = w["temp"]
                high = w["high"]
                low = w["low"]

                say(f'The current weather in {city} is {desc} and {temp} degrees with a high of {high} and a low of {low}.')

            elif "joke" in c:
                say(jokes.jokes)

            elif "date" in c:
                date = datetime.now().strftime('%A %B %d %Y')
                say(f"The current date is {date}")

            elif "time" in c:
                t = time.strftime('%H:%M', time.localtime())
                h = int(t.split(":")[0])
                post = "p m" if (h >= 12) else "a m"
                h = h%12
                m = t.split(":")[1]
                say(f'The current time is {h, m, post}')

            elif "bye" in c:
                say("goodbye")
                break


if __name__ == '__main__':
    while True:
        listen()