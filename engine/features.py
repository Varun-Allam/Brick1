import os
from playsound import playsound

def playAssistantSound():
    # Build correct absolute path
    music_dire = os.path.join(
        os.getcwd(),
        "www/assets/audio/www_assets_audio_start_sound.mp3"
    )

    print("Playing:", music_dire)  # debug print
    playsound(music_dire)