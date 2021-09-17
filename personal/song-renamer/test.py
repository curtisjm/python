import requests

url = "https://v1.nocodeapi.com/matchachacha_/spotify/mYLqriUfCBqFUJAg/playlists?id=1gmmKUoTBmGb0zjVX8dSy0"
params = {}
r = requests.get(url=url, params=params)
result = r.json()

songs = []

for item in result["tracks"]["items"]:
    song = item["track"]["name"]
    artist = item["track"]["artists"][0]["name"]
    songs.append([song, artist])

[print(f"{song[0]} - {song[1]}") for song in songs]
