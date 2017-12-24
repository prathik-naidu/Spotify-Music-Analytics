import json
import spotipy
import time
import sys
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
from dateutil.parser import parse

def get_songs(userID, playlistID, sp):
    results = sp.user_playlist_tracks('12165262567', '11Fo4ON0gWVQ56aPXgjOk3')
    songs = results['items']
    ids = []
    while results['next']:
        results = sp.next(results)
        songs.extend(results['items'])

    for i in songs:
        ids.append(i['track']['id'])

    return ids, songs

#Get Audio Features for a Playlist
def get_audio_features(ids, songs, sp):
    results = sp.user_playlist_tracks('12165262567', '11Fo4ON0gWVQ56aPXgjOk3')
    index = 0
    length_feature = []
    popularity_feature = []
    explicit_feature = []
    audio_features = []


    #songs = results['items']
    #print(songs[0]['added_at'])
    for i in songs:
        length_feature.append(i['track']['duration_ms'])
        popularity_feature.append(i['track']['popularity'])
        explicit_feature.append(i['track']['explicit'])

    while index < len(ids):
        audio_features += sp.audio_features(ids[index:index + 50])
        index += 50

    features_list = []
    for features in audio_features:
        features_list.append([features['energy'], features['liveness'],
            features['tempo'], features['speechiness'],
            features['acousticness'], features['instrumentalness'],
            features['time_signature'], features['danceability'],
            features['key'], features['duration_ms'],
            features['loudness'], features['valence'],
            features['mode']])

    df = pd.DataFrame(features_list, columns=['energy', 'liveness',
                                                  'tempo', 'speechiness',
                                                  'acousticness', 'instrumentalness',
                                                  'time_signature', 'danceability',
                                                  'key', 'duration_ms', 'loudness',
                                                  'valence', 'mode'])

    df = df.assign(length = length_feature)
    df = df.assign(popularity = popularity_feature)
    df = df.assign(explicit = explicit_feature)

    writer = pd.ExcelWriter('/Users/Prathik/Desktop/output2.xlsx')
    df.to_excel(writer, 'Sheet1')


def preprocess_data(like, dislike):
    like.loc[like['explicit'] == "TRUE", 'explicit'] = 1
    dislike.loc[dislike['explicit'] == "FALSE", 'explicit'] = 0
    dislike.loc[dislike['explicit'] == "TRUE", 'explicit'] = 1
    dislike.loc[dislike['explicit'] == "FALSE", 'explicit'] = 0

    like['target'] = 1
    dislike['target'] = 0

    complete_data = pd.concat([like,dislike], ignore_index = True)

    return complete_data


#Get Playlist Code
def get_playlist_ID(userID, sp):
    playlists = sp.user_playlists()
    playlist_map = collections.defaultdict(str)
    while playlists:
        for i, playlist in enumerate(playlists['items']):
            print("%3d %s %s" % (i + 1 + playlists['offset'], playlist['name']))
            playlist_map[i + 1 + playlists['offset']] = playlist['name']
        if playlists['next']:
            playlists = sp.next(playlists)
        else:
            playlists = None

    num = input('Choose a desired playlist to analyze by entering the corresponding number: ')
    like = input('Choose playlists that you enjoy listening to (enter each playlist number space separated): ')
    dislike = input('Choose plyalists that you do not enjoy (enter each plyalist number space separated): ')
    return like, dislike, playlist_map[int(num)]

'''def main(userID, playlistID):
    client_credentials_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    #print("Getting user playlist")
    #get_user_playlist(username, sp)
    #print("Getting playlist content")
    #get_playlist_content(username, playlist, sp)
    #print("Getting playlist audio features")
    song_ids = get_songs(userID, playlistID, sp)
    df_features = get_audio_features(song_ids)


if __name__ == '__main__':
    print 'Starting...'
    parser = argparse.ArgumentParser(description='description')
    parser.add_argument('--username', help='username')
    parser.add_argument('--playlist', help='username')
    args = parser.parse_args()
    main('12165262567', '11Fo4ON0gWVQ56aPXgjOk3')'''






