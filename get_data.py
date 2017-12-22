import json
import spotipy
import time
import sys
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#Get Playlist Code
#playlists = sp.user_playlists('12165262567')
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

#Get Audio Features for a Playlist
#content = sp.user_playlist_tracks('12165262567', '11Fo4ON0gWVQ56aPXgjOk3', fields=None, limit=100, market=None)
results = sp.user_playlist_tracks('12165262567', '11Fo4ON0gWVQ56aPXgjOk3')
songs = results['items']
while results['next']:
    results = sp.next(results)
    songs.extend(results['items'])


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

writer = pd.ExcelWriter('/Users/Prathik/Desktop/output.xlsx')
df.to_excel(writer, 'Sheet1')



def main(username, playlist):
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    print "Getting user playlist"
    get_user_playlist(username, sp)
    print "Getting playlist content"
    get_playlist_content(username, playlist, sp)
    print "Getting playlist audio features"
    get_playlist_audio_features(username, playlist, sp)


if __name__ == '__main__':
    print 'Starting...'
    parser = argparse.ArgumentParser(description='description')
    parser.add_argument('--username', help='username')
    parser.add_argument('--playlist', help='username')
    args = parser.parse_args()
    main(args.username, args.playlist)






