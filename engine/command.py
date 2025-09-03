import pyttsx3
import speech_recognition as sr
import eel 


def speak(text):
    engine = pyttsx3.init('nsss')  # 'nsss' = macOS driver
    voices = engine.getProperty('voices')
    
    # Pick a voice (list them first to choose the right index)
    engine.setProperty('voice', voices[3].id)
    engine.setProperty('rate', 150)
    
    engine.say(text)
    engine.runAndWait()

 
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...') 
        eel.DisplayMessage('listening...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout=10, phrase_time_limit=6)

    try:
        print('recognizing...') 
        eel.DisplayMessage('recognizing...')
        # use Google recognizer (works without API key)
        query = r.recognize_google(audio, language='english')
        print(f"user said: {query}")  
        eel.DisplayMessage(query)
        speak(query) 
        eel.ShowHood()
    except Exception as e:
       return ""
    return query.lower()  

@eel.expose
def allCommand(): 
    query = takecommand() 
    print(query)
