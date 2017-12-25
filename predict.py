import spotipy
import sys
import pandas as pd
import numpy as np
from spotipy.oauth2 import SpotifyClientCredentials
from get_data import get_audio_features, get_songs, get_playlist_ID, preprocess_data
from model import separate_features, split_data, kNN_model, rf_model
import argparse
import spotipy.util as util
import os
from json.decoder import JSONDecodeError
import collections


def main(userID):
    client_credentials_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    #Setup Spotify Authentication Protocol
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
	
	#Get Consolidated Dataset for selected like and disliked songs
    like, dislike, analyze = get_playlist_ID(userID, sp)
    like_final = pd.DataFrame()
    dislike_final = pd.DataFrame()

    for pair in like:
    	playlist = pair[0]
    	userID = pair[1]
    	like_ids, like_songs = get_songs(userID, playlist, sp)
    	like_audio_features = get_audio_features(like_ids, like_songs, sp)
    	like_final = pd.concat([like_final, like_audio_features], ignore_index = True)

    for pair in dislike:
    	playlist = pair[0]
    	userID = pair[1]
    	dislike_ids, dislike_songs = get_songs(userID, playlist, sp)
    	dislike_audio_features = get_audio_features(dislike_ids, dislike_songs, sp)
    	dislike_final = pd.concat([dislike_final, dislike_audio_features], ignore_index = True)

    #Preprocess data to get a "target" column
    complete_data = preprocess_data(like_final, dislike_final)

    #Seperate features into features and labels dataset
    X, y = separate_features(complete_data)

    #Split data into training and test dataset
    X_train, X_test, y_train, y_test = split_data(X, y)

    #Reshape dimensions of labels (y)
    y_train = np.ravel(y_train)
    y_test = np.ravel(y_test)
    
    rf_model(X_train, X_test, y_train, y_test)



if __name__ == '__main__':
    print('Starting... \n\n')
    parser = argparse.ArgumentParser(description='description')
    parser.add_argument('--username', help='username')
    parser.add_argument('--playlist', help='username')
    args = parser.parse_args()
    main('12165262567')