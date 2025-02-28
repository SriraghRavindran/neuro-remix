from pydub import AudioSegment
import random

def change_mood(file_path, mood="happy"):
    """Apply transformations to change mood of the audio."""
    audio = AudioSegment.from_file(file_path)

    if mood == "happy":
        # Increase tempo & pitch slightly
        audio = audio.speedup(playback_speed=1.1)
    elif mood == "sad":
        # Slow down and lower pitch
        audio = audio.speedup(playback_speed=0.9)
    elif mood == "lofi":
        # Add slight reverb and noise reduction
        audio = audio.low_pass_filter(3000)

    output_path = file_path.replace("input", "output").replace(".mp3", f"_{mood}.mp3")
    audio.export(output_path, format="mp3")
    return output_path

