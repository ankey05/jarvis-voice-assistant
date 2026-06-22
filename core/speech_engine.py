# Purpose: handle all speaking.

import pyttsx3
import time

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

def speak(text):
    try:
        print(f"Speaking: {text}")  # Debug print
        engine.say(text)
        engine.runAndWait()
        time.sleep(0.5)
    except Exception as e:
        print(f"Speak error: {e}")