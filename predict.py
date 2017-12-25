import spotipy
import sys
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
from get_data import get_audio_features, get_songs, get_playlist_ID
import argparse
import spotipy.util as util
import os
from json.decoder import JSONDecodeError
import collections


def main(userID):
    client_credentials_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    #print("Getting user playlist")
    #get_user_playlist(username, sp)
    #print("Getting playlist content")
    #get_playlist_content(username, playlist, sp)
    #print("Getting playlist audio features")

    #song_ids, songs = get_songs(userID, playlistID, sp)
    #df_features = get_audio_features(song_ids, songs, sp)
    #like, dislike, value = get_playlist_ID(userID, sp)

    scope = 'playlist-read-private'
    username = userID
    try:
    	token = util.prompt_for_user_token(username, scope)
    except(AttributeError, JSONDecodeError):
    	os.remove(f".cache-{username}")
    	token = util.prompt_for_user_token(username, scope)

    if token:
    	sp = spotipy.Spotify(auth=token)
    	sp.trace = False

    like, dislike, analyze = get_playlist_ID(userID, sp)



    like = '11Fo4ON0gWVQ56aPXgjOk3'
    dislike = 'spotify:user:12165262567:playlist:669fXEh1Qc7EusoybzI7V8'

if __name__ == '__main__':
    print('Starting...')
    parser = argparse.ArgumentParser(description='description')
    parser.add_argument('--username', help='username')
    parser.add_argument('--playlist', help='username')
    args = parser.parse_args()
    main('12165262567')