import time
import spotipy as spotipy
from spotipy import SpotifyOAuth
import logging

from env import USER_ID

SCOPE="playlist-modify-public playlist-modify-private playlist-read-private playlist-read-collaborative user-read-currently-playing"

logger = logging.getLogger('app')
logging.basicConfig(level='DEBUG')

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE))


def get_playlist_id():

    # gets list of user playlists
    playlists = sp.current_user_playlists()['items']

    # iterate though playlists to check if 'agent of chaos' exists
    for playlist in range(len(playlists)):
        if playlists[playlist]['name'] == 'agent of chaos':
            logger.info('Playlist already exists')
            return playlists[playlist]['id']

    # creates playlist if one doesn't exists
    return sp.user_playlist_create(USER_ID, "agent of chaos", True, False, "under construction")['id']


if __name__ == '__main__':

    playlist_id = get_playlist_id()



    current_track_id = None
    while True:
        current_track_info = sp.currently_playing()
        if current_track_info['item']['id'] != current_track_id:
            sp.playlist_add_items(playlist_id, [current_track_info['item']['uri']])
            current_track_id = current_track_info['item']['id']

        time.sleep(50)