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



@eel.expose

def playAssistantSound2():
    # Build correct absolute path
    music_dire = os.path.join(
        os.getcwd(),
        "www/assets/audio/www_assets_audio_start_sound.mp3"
    )

    print("Playing:", music_dire)  # debug print
    playsound(music_dire)     




