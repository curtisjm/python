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

results = sp.search(q="caravan", limit=1)
print(results)
# for idx, track in enumerate(results["tracks"]["items"]):
#     print(
#         "Song: "
#         + str(track["name"])
#         + "    Artist: "
#         + str(track["artists"][0]["name"])
#     )
