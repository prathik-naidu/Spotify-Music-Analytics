import json
import spotipy
import time
import sys
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#Get Playlist
playlists = sp.user_playlists('12165262567')
'''while playlists:
    for i, playlist in enumerate(playlists['items']):
        print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None'''


offset = 0
songs = []
items = []
ids = []

content = sp.user_playlist_tracks('12165262567', '11Fo4ON0gWVQ56aPXgjOk3', fields=None, limit=100, market=None)
print(content)
songs += content['items']
#if content['next'] is not None:
#    offset += 100
#else:
#    break

#print("HELLO")
#print(songs)
for i in songs:
    ids.append(i['track']['id'])

index = 0
audio_features = []
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
        features['mode'], features['type'],
        features['uri']])

df = pd.DataFrame(features_list, columns=['energy', 'liveness',
                                              'tempo', 'speechiness',
                                              'acousticness', 'instrumentalness',
                                              'time_signature', 'danceability',
                                              'key', 'duration_ms', 'loudness',
                                              'valence', 'mode', 'type', 'uri'])

#print(df)


tid = 'spotify:track:4TTV7EcfroSLWzXRY6gLv6'

tids = ['spotify:track:4TTV7EcfroSLWzXRY6gLv6','spotify:track:3JIxjvbbDrA9ztYlNcp3yL']

'''start = time.time()
analysis = sp.audio_analysis(tid)
delta = time.time() - start
print(json.dumps(analysis, indent=4))
print ("analysis retrieved in %.2f seconds" % (delta,))'''

start = time.time()
features = sp.audio_features(tid)

#print(features)
#print(features['energy'])

delta = time.time() - start
'''for feature in features:
    print(json.dumps(feature, indent=4))
    print()
    analysis = sp._get(feature['analysis_url'])
    print(json.dumps(analysis, indent=4))
    print()'''
print ("features retrieved in %.2f seconds" % (delta,))
