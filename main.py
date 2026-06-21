
from listener import listen
from jarvis_commands import process
from speech_engine import engine
from speech_engine import speak
# speak("jarvis is starting")

import time

def main():

    speak("Initializing Jarvis")

    while True:
        word = listen()
        print("Wake word heard: ", word)

        if word and "jarvis" in word:
            
            engine.say("Yes sir, how may I help you")
            
            time.sleep(3)
            engine.runAndWait()
 
            command = listen()
            print("Command heard:", command)
            print("Recieved command", command)
            if command:
                print("processing: ", command)
                process(command)

if __name__ == "__main__":
    main()