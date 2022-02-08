import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import setup

client_credentials_manager = SpotifyClientCredentials(client_id=setup.CLIENT_ID, client_secret=setup.CLIENT_SECRET) 
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

streaming_df0 = pd.read_json('/Users/vineethravella/Desktop/DS_Projects/myspotify_project/data/raw_streaming_data/StreamingHistory0.json')
streaming_df1 = pd.read_json('/Users/vineethravella/Desktop/DS_Projects/myspotify_project/data/raw_streaming_data/StreamingHistory1.json')
streaming_df2 = pd.read_json('/Users/vineethravella/Desktop/DS_Projects/myspotify_project/data/raw_streaming_data/StreamingHistory2.json')
df_list = [streaming_df0, streaming_df1, streaming_df2]
streaming_df = pd.concat(df_list)
artist = streaming_df['artistName'].values[1]
track = streaming_df['trackName'].values[1]
print(artist)
print(track)
result = sp.search(q='artist:' + artist + ' track:' + track, type='track')
print(result['tracks']['items'][0]['id'])

def get_track_id(x):
    try:
        artist = x.artistName
        track = x.trackName
        result = sp.search(q='artist:' + artist + ' track:' + track, type='track')
        return result['tracks']['items'][0]['id']
    except:
        return None


streaming_df['track_id'] = streaming_df.apply(get_track_id, axis=1)
streaming_df.to_csv('streaming_track.csv')