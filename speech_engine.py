# Purpose: handle all speaking.

import pyttsx3
engine = pyttsx3.init()
# engine.say("hello aniket")
# engine.runAndWait

def speak(text):
    engine.say(text)
    engine.runAndWait()