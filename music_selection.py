from decouple import config
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from helper import format_for_disc_prompt


def get_music_selection(playlist_id):
    CLIENT_ID = config('CLIENT_ID')
    CLIENT_SECRET = config('CLIENT_SECRET')

    client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    playlist_id = playlist_id

    playlist_tracks = sp.playlist_tracks(playlist_id)

    track_and_artist = {}

    for track in playlist_tracks['items']:
        track_and_artist[track['track']['name']] = track['track']['artists'][0]['name']
    
    return format_for_disc_prompt(track_and_artist)

