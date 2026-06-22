import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak Something.....")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
    print("You Said:", text)

except:
    print("Sorry, could you understand.")