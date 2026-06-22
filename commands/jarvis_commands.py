import webbrowser
from core.speech_engine import speak


def process(commands):

    print("Command received: ",  commands)

    if "open google" in commands.lower():
        speak("opening google")
        webbrowser.open("https://google.com")

    elif "open youtube" in commands.lower():
        speak("opening youtube")
        webbrowser.open("https://youtube.com")

    elif "open spotify" in commands.lower():
        speak("opening spotify")
        webbrowser.open("https://spotify.com")

    elif "open github" in commands.lower():
        speak("opening github")
        webbrowser.open("https://github.com")

    elif "open whatsapp" in commands.lower():
        speak("opening whatsapp")
        webbrowser.open("https://web.whatsapp.com")

    else:
        speak("Sorry sir, I didn't understand")