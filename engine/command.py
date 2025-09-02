import pyttsx3
import speech_recognition as sr

def speak(text):
    engine = pyttsx3.init('nsss')  # 'nsss' = macOS driver
    voices = engine.getProperty('voices')
    
    # Pick a voice (list them first to choose the right index)
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 174)
    
    engine.say(text)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout=10, phrase_time_limit=8)

    try:
        print('recognizing...')
        # use Google recognizer (works without API key)
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
    except Exception as e:
        print("Error:", e)
        return ""
    return query.lower()

text = takecommand()
speak(text if text else "I did not catch that")