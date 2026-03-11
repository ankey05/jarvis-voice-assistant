# Responsible for microphone + speech recognition.

# import speech_recognition as sr

# r = sr.Recognizer()

# def listen():
#     try:
#         with sr.Microphone() as source:
#             print("Listening...")
#             r.adjust_for_ambient_noise(source)
#             audio = r.listen(source, timeout=5, phrase_time_limit=4)

#         text = r.recognize_google(audio)
#         print("Heard:", text)

#         return text.lower()

#     except Exception as e:
#         print("Error:", e)
#         return ""

import speech_recognition as sr

r = sr.Recognizer()

def listen():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source, timeout=5, phrase_time_limit=4)

        text = r.recognize_google(audio)
        print("Heard:", text)

        return text.lower()

    except Exception as e:
        print("Error:", e)
        return ""
                    
