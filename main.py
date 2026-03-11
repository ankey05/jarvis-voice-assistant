
from listener import listen
from jarvis_commands import process
from speech_engine import speak

def main():

    speak("Initializing Jarvis")

    while True:
        word = listen()

        if word and "jarvis" in word:
            speak("Yes sir, how may I help you")

            command = listen()
            print("Recieved command", command)
            if command:
                process(command)

if __name__ == "__main__":
    main()