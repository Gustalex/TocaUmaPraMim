def format_for_disc_prompt(music_data):
    formatted_data = []
    for track, name in music_data.items():
        formatted_data.append(f' m!p {track} {name}')
    return formatted_data

    