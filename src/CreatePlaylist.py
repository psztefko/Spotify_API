import json
import requests

from env import SPOTIFY_USER_ID, SPOTIFY_ACCESS_TOKEN


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
        pass

    def add_song_to_playlist(self):
        pass