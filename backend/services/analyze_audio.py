import librosa
import numpy as np

def analyze_audio(file_path):
    y, sr = librosa.load(file_path,sr=None)
     # Extract tempo
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)

    # Extract key
    chroma = librosa.feature.chroma_stft(y=y, sr=sr)
    key = np.argmax(np.mean(chroma, axis=1))

    # Estimate mood using spectral centroid
    spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr).mean()
    mood = "Energetic" if spectral_centroid > 3000 else "Calm"

    return {
        "tempo": round(float(tempo), 2),
        "key": int(key),
        "mood": mood
    }