import os
import re
from playsound import playsound 
import eel
from engine.config import Assistant_Name 
from engine.command import speak 
import pywhatkit as kit

@eel.expose

def playAssistantSound():
    # Build correct absolute path
    music_dire = os.path.join(
        os.getcwd(),
        "www/assets/audio/siri.mp3"
    )

    print("Playing:", music_dire)  # debug print
    playsound(music_dire)      



@eel.expose

def playAssistantSound2():
    # Build correct absolute path
    music_dire = os.path.join(
        os.getcwd(),
        "www/assets/audio/www_assets_audio_start_sound.mp3"
    )

    print("Playing:", music_dire)  # debug print
    playsound(music_dire)     




def openCommand(query): 
    query = query.replace(Assistant_Name, "") 
    query = query.replace("open","") 
    query.lower() 

    if query != "": 
        speak("opening "+query) 
        os.system('open -a '+query) 
    else: 
        speak("not found")

def platYoutube(query):
    search_term = extract_yt_term(query)
    speak("playing "+search_term+" on youtube") 
    kit.playonyt(search_term) 

def extract_yt_term(command):
    #def a regular expression pattern 
    pattern = r'play\s+(.*?)\s+on\s+youtube' 
    #use re.search to find command 
    match = re.search(pattern,command,re.IGNORECASE) 
    #if a match found 
    return match.group(1) if match else None