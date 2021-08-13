import argparse
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from env import SCOPE
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


def main():

    hello_world()
    # sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE))
    #
    # results = sp.current_user_saved_tracks()
    # for idx, item in enumerate(results['items']):
    #     track = item['track']
    #     print(idx, track['artists'][0]['name'], " – ", track['name'])





    # spotify = CreatePlaylist()
    #
    # current_track_id = None
    # while True:
    #     current_track_info = spotify.get_current_track()
    #
    #     if current_track_info['id'] != current_track_id:
    #         print(current_track_info)
    #         spotify.add_song_to_playlist(current_track_info['uri'], spotify.get_playlist_id())
    #         current_track_id = current_track_info['id']
    #
    #     time.sleep(2)



if __name__ == '__main__':
    main()
