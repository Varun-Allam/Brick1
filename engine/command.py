import pyttsx3


def speak(text):
    engine = pyttsx3.init('nsss') 
    voices=engine.getProperty('voices') 
    engine.setProperty('voice',voices[2].id) 
    engine.setProperty('rate', 174)
    print(voices)
    engine.say(text)
    engine.runAndWait()    

speak("I Love india")