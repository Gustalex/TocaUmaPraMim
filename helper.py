import random

def format_for_disc_prompt(music_data):
    formatted_data = []
    for track, name in music_data.items():
        formatted_data.append(f' m!p {track} {name}')
    return formatted_data

def randomize_music_selection(music_data):
    random.shuffle(music_data)
    return music_data
    