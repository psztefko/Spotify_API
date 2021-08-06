from env import SPOTIFY_USER_ID, SPOTIFY_ACCESS_TOKEN, SPOTIFY_GET_CURRENT_TRACK_URL
from src.CreatePlaylist import CreatePlaylist
import time
import json
import requests

def create_playlist():
    """Create A New Playlist"""

    request_body = json.dumps({
        "name": "Youtube Liked Vids",
        "description": "All Liked Youtube Videos",
        "public": True
    })

    query = "https://api.spotify.com/v1/users/{}/playlists".format(
        SPOTIFY_USER_ID)
    response = requests.post(
        query,
        data=request_body,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {SPOTIFY_ACCESS_TOKEN}"
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

def get_current_song(access_token):
    response = requests.get(
        SPOTIFY_GET_CURRENT_TRACK_URL,
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )
    json_resp = response.json()

    track_id = json_resp['item']['id']
    track_name = json_resp['item']['name']
    artists = [artist for artist in json_resp['item']['artists']]

    link = json_resp['item']['external_urls']['spotify']

    artist_names = ', '.join([artist['name'] for artist in artists])

    current_track_info = {
    	"id": track_id,
    	"track_name": track_name,
    	"artists": artist_names,
    	"link": link
    }

    return current_track_info

def add_song_to_playlist():
    """Add all liked songs into a new Spotify playlist"""

    # get uri of current song
    current_song = get_current_song()
    uri = current_song['uri']

    # create a new playlist
    playlist_id = create_playlist()

    # add song into playlist
    request_data = json.dumps(uri)

    query = "https://api.spotify.com/v1/playlists/{}/tracks".format(
        playlist_id)

    response = requests.post(
        query,
        data=request_data,
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(SPOTIFY_ACCESS_TOKEN)
        }
    )

    response_json = response.json()
    return response_json


def main():

    get_current_song(SPOTIFY_ACCESS_TOKEN)
    #create_playlist()
    # current_track_id = None
    # while True:
    #     current_track_info = get_current_song()
    #
    #     if current_track_info['id'] != current_track_id:
    #         add_song_to_playlist()
    #         current_track_id = current_track_info['id']
    #
    #     time.sleep(2)


if __name__ == '__main__':
    main()
