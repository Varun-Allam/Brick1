import os
from playsound import playsound 
import eel


@eel.expose

def playAssistantSound():
    # Build correct absolute path
    music_dire = os.path.join(
        os.getcwd(),
        "www/assets/audio/siri.mp3"
    )

    print("Playing:", music_dire)  # debug print
    playsound(music_dire)     



