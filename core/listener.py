# import speech_recognition as sr

# r = sr.Recognizer()

# def listen():
#     try:
#         with sr.Microphone() as source:
#             print("Listening...")
#             r.adjust_for_ambient_noise(source, duration=1)
#             audio = r.listen(source, timeout=5, phrase_time_limit=6)
        
#         text = r.recognize_google(audio)
#         print("Heard:", text)
#         return text.lower()

#     except sr.UnknownValueError:
#         print("Error: Could not understand audio")
#         return ""
    
#     except sr.RequestError as e:
#         print(f"Error: Network/API issue - {e}")
#         return ""
    
#     except sr.Timeout:
#         print("Error: No speech detected (timeout)")
#         return ""
    
#     except Exception as e:
#         print(f"Error: {type(e).__name__} - {e}")
#         return ""

import speech_recognition as sr

r = sr.Recognizer()

def listen():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source, timeout=5, phrase_time_limit=6)
        
        text = r.recognize_google(audio)
        print("Heard:", text)
        return text.lower()

    except sr.UnknownValueError:
        print("Error: Could not understand audio")
        return ""
    
    except sr.RequestError as e:
        print(f"Error: Network/API issue - {e}")
        return ""
    
    except sr.exceptions.WaitTimeoutError:  # ✅ CORRECT
        print("Error: No speech detected (timeout)")
        return ""
    
    except Exception as e:
        print(f"Error: {type(e).__name__} - {e}")
        return ""