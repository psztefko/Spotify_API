from src.Spotify import CreatePlaylist
import time


def main():

    spotify = CreatePlaylist()

    current_track_id = None
    while True:
        current_track_info = spotify.get_current_track()

        if current_track_info['id'] != current_track_id:
            print(current_track_info)
            spotify.add_song_to_playlist(current_track_info['uri'], spotify.get_playlist_id())
            current_track_id = current_track_info['id']

        time.sleep(5)


if __name__ == '__main__':
    main()
