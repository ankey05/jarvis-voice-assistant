
from core.listener import listen
from commands.jarvis_commands import process
from core.speech_engine import speak
import time

def main():

    speak("Initializing Jarvis")

    while True:
        word = listen()
        print("Wake word heard: ", word)

        if word and "jarvis" in word:
            speak("Yes sir, how may I help you")
            time.sleep(1)

            command = listen()
            print("Recieved command", command)
            if command:
                process(command)

if __name__ == "__main__":
    main()