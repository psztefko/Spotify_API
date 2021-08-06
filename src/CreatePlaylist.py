import json
import requests

from env import SPOTIFY_USER_ID, SPOTIFY_ACCESS_TOKEN, SPOTIFY_GET_CURRENT_TRACK_URL


class CreatePlaylist:

    def __init__(self):
        pass

    def create_playlist(self):
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
                "Authorization": "Bearer {}".format(SPOTIFY_ACCESS_TOKEN)
            }
        )
        response_json = response.json()

        # playlist id
        return response_json["id"]

    def get_current_song(self):
        response = requests.get(
            SPOTIFY_GET_CURRENT_TRACK_URL,
            headers={
                "Authorization": f"Bearer {SPOTIFY_ACCESS_TOKEN}"
            }
        )
        json_resp = response.json()

        track_id = json_resp['item']['id']
        uri = json_resp['item']['uri']

        current_track_info = {
            "id": track_id,
            "uri": uri,
        }

        return current_track_info

    def add_song_to_playlist(self):
        """Add all liked songs into a new Spotify playlist"""

        # get uri of current song
        current_song = self.get_current_song()
        uri = current_song['uri']

        # create a new playlist
        playlist_id = self.create_playlist()

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