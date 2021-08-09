#from src.CreatePlaylist import CreatePlaylist
from env import SPOTIFY_USER_ID, ACCESS_TOKEN, SPOTIFY_GET_CURRENT_TRACK_URL
from pprint import pprint
import time
import json
import requests

def create_playlist():
    """Create A New Playlist"""

    request_body = json.dumps({
        "name": "agent of chaos",
        "description": "under construction",
        "public": True
    })

    query = "https://api.spotify.com/v1/users/{}/playlists".format(
        SPOTIFY_USER_ID)
    response = requests.post(
        query,
        data=request_body,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {ACCESS_TOKEN}"
        }
    )
    response_json = response.json()

    # playlist id
    return response_json["id"]


# def get_current_song():
#     response = requests.get(
#         SPOTIFY_GET_CURRENT_TRACK_URL,
#         headers={
#             "Authorization": f"Bearer {SPOTIFY_ACCESS_TOKEN}"
#         }
#     )
#     json_resp = response.json()
#
#     track_id = json_resp['item']['id']
#     uri = json_resp['item']['uri']
#
#     current_track_info = {
#         "id": track_id,
#         "uri": uri,
#     }
#
#     return current_track_info


def add_song_to_playlist():
    """Add current playing song into a new Spotify playlist
    playlist_id: 3cEYpjA9oz9GiPac4AsH4n
    song_uri: """



def get_current_track():
    response = requests.get(
        SPOTIFY_GET_CURRENT_TRACK_URL,
        headers={
            "Authorization": f"Bearer {ACCESS_TOKEN}"
        }
    )
    json_resp = response.json()

    track_id = json_resp['item']['id']
    track_name = json_resp['item']['name']
    artists = [artist for artist in json_resp['item']['artists']]
    link = json_resp['item']['external_urls']['spotify']
    artist_names = ', '.join([artist['name'] for artist in artists])

    uri = json_resp['item']['uri']

    current_track_info = {
    	"id": track_id,
    	"track_name": track_name,
    	"artists": artist_names,
    	"link": link,
        "uri": uri
    }

    return current_track_info


def main():
    current_track_id = None
    while True:
        current_track_info = get_current_track()

        if current_track_info['id'] != current_track_id:
            pprint(
                current_track_info,
                indent=4,
            )
            current_track_id = current_track_info['id']

        time.sleep(1)


if __name__ == '__main__':
    main()