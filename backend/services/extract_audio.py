import yt_dlp
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
import asyncio

# SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
# SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

# sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
#     client_id=SPOTIFY_CLIENT_ID,
#     client_secret=SPOTIFY_CLIENT_SECRET
# ))

async def download_youtube_audio(url, output_path="data/input/"):
    """Download audio from a YouTube URL."""
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'}],
        'ffmpeg_location': 'C:/ffmpeg/bin',
    }
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, yt_dlp.YoutubeDL(ydl_opts).download, [url])

# def get_spotify_track_info(url):
#     """Retrieve track metadata from Spotify URL."""
#     track_id = url.split("/")[-1].split("?")[0]
#     track_info = sp.track(track_id)
#     return {
#         "title": track_info["name"],
#         "artist": track_info["artists"][0]["name"],
#         "tempo": track_info["tempo"] if "tempo" in track_info else None
#     }
