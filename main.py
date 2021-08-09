#from src.CreatePlaylist import CreatePlaylist
from env import USER_ID, ACCESS_TOKEN, GET_CURRENT_TRACK_URL, GET_LIST_OF_USER_PLAYLISTS
from pprint import pprint
import time
import json
import requests
import logging

logger = logging.getLogger('main')
logging.basicConfig(level=logging.DEBUG)

def create_playlist():
    """Creates new playlist"""

    request_body = json.dumps({
        "name": "agent of chaos",
        "description": "under construction",
        "public": False
    })

    query = "https://api.spotify.com/v1/users/{}/playlists".format(
        USER_ID)
    response = requests.post(
        query,
        data=request_body,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {ACCESS_TOKEN}"
        }
    )

    logger.info('Playlist created')

    json_resp = response.json()
    return json_resp['id']


def get_list_of_playlists():
    """Returns list of current user playlists"""

    response = requests.get(
        GET_LIST_OF_USER_PLAYLISTS,
        headers={
            "Authorization": f"Bearer {ACCESS_TOKEN}"
        }
    )
    json_resp = response.json()
    return json_resp['items']

def get_playlist_id():
    """Checks user playlists and if dump playlist doesn't exist, creates it"""

    playlists = get_list_of_playlists()

    for playlist in range(len(playlists)):
        if playlists[playlist]['name'] == 'agent of chaos':
            return playlists[playlist]['id']

    create_playlist()

    for playlist in range(len(playlists)):
        if playlists[playlist]['name'] == 'agent of chaos':
            pass



def add_song_to_playlist():
    """Add current playing song into a playlist
    playlist_id: 3cEYpjA9oz9GiPac4AsH4n
    song_uri: """



def get_current_track():
    """Gets current playing track info"""

    response = requests.get(
        GET_CURRENT_TRACK_URL,
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

    logger.info('Received current track info')
    return current_track_info


def main():

    create_playlist()

    # current_track_id = None
    # while True:
    #     current_track_info = get_current_track()
    #
    #     if current_track_info['id'] != current_track_id:
    #         pprint(
    #             current_track_info,
    #             indent=4,
    #         )
    #         current_track_id = current_track_info['id']
    #
    #     time.sleep(1)


if __name__ == '__main__':
    main()