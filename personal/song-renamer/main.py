import os
import re

root_dir = "./songs/"

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

for dance in dance_dirs:
    if dance.replace("/", "") not in os.listdir(root_dir):
        print(f"{dance} folder does not exist. Moving onto the next one...")
        continue

    songs = os.listdir(root_dir + dance)

    for song in songs:
        string_changed = False
        new_song_name = song

        try:
            if "{" in song:
                new_song_name = re.sub(r"\{[^()]*\}", "", song)
            if "(" in song:
                new_song_name = re.sub(r"\([^()]*\)", "", song)
            if "[" in song:
                new_song_name = re.sub(r"\[[^()]*\]", "", song)

            for str in remove_strings:
                if str in new_song_name:
                    new_song_name = new_song_name.replace(str, "", -1)
                    string_changed = True

            if "  " in new_song_name:
                new_song_name = new_song_name.replace("  ", " ", -1)

            if " ." in new_song_name:
                new_song_name = new_song_name.replace(" .", ".", -1)

            os.rename(root_dir + dance + song, root_dir + dance + new_song_name)
        except FileExistsError:
            print(
                f"Error, new name {new_song_name} already exists. Adding a 2 to it..."
            )
            os.rename(root_dir + dance + song, +root_dir + dance + new_song_name)
        except Exception as e:
            print("An unknown error has occurrend")
            print(e)

        if string_changed:
            print(f"{song} was changed to {new_song_name}")
