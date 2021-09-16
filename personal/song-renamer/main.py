import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

load_dotenv()

sp = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(
        client_id=os.getenv("CLIENT_ID"), client_secret=os.getenv("CLIENT_SECRET")
    )
)

root_dir = "./"

dance_dirs = [
    "Waltz/",
    "Tango/",
    "Foxtrot/",
    "Viennese Waltz/",
    "Quickstep/",
    "Cha Cha/",
    "Samba/",
    "Rumba/",
    "Paso/",
    "Jive/",
]

remove_strings = [
    "bpm",
    "BPM",
    "Bpm",
    "Official Song",
    "Official Video",
    "Audio",
    "Video",
    "Lyrics",
    "Lyric",
]

# old_name: new_name
old_and_new_names = {}

for dance in dance_dirs:
    if dance.replace("/", "") not in os.listdir(root_dir):
        print(f"{dance} folder does not exist. Moving onto the next one...")
        continue

    songs = os.listdir(root_dir + dance)

    for song in songs:
        results = sp.search(q=song, limit=1)
        track = enumerate(results["tracks"]["items"])
        old_and_new_names[song] = {
            "track": str(track["name"]),
            "artist": str(track["artists"][0]["name"]),
        }

    [print(name) for name in old_and_new_names]
    old_and_new_names = {}
