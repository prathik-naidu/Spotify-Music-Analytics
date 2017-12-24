import spotipy
import sys
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
from get_data import get_audio_features, get_songs
import argparse

def main(userID, playlistID):
    client_credentials_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    #print("Getting user playlist")
    #get_user_playlist(username, sp)
    #print("Getting playlist content")
    #get_playlist_content(username, playlist, sp)
    #print("Getting playlist audio features")
    song_ids, songs = get_songs(userID, playlistID, sp)
    df_features = get_audio_features(song_ids, songs, sp)


if __name__ == '__main__':
    print 'Starting...'
    parser = argparse.ArgumentParser(description='description')
    parser.add_argument('--username', help='username')
    parser.add_argument('--playlist', help='username')
    args = parser.parse_args()
    main('12165262567', '11Fo4ON0gWVQ56aPXgjOk3')