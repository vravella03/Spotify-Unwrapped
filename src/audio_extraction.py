import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import setup

client_credentials_manager = SpotifyClientCredentials(client_id=setup.CLIENT_ID, client_secret=setup.CLIENT_SECRET) 
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

streaming_df_final = pd.read_csv('streaming_track.csv')
temp_df = pd.DataFrame()

def get_track_details(x):
    return sp.track(x)

def get_track_features(x):
    return sp.audio_features(x)

def get_album(x):
    try:
        track_details = get_track_details(x)
        album_name = track_details['album']['name']
        return album_name
    except:
        return None

def get_release_date(x):
    try:
        track_details = get_track_details(x)
        release_date = track_details['album']['release_date']
        return release_date
    except:
        return None

def get_track_length(x):
    try:
        track_details = get_track_details(x)
        duration = track_details['duration_ms']
        return duration
    except:
        return None

def get_popularity(x):
    try:
        track_details = get_track_details(x)
        popularity = track_details['popularity']
        return popularity
    except:
        return None

def get_acousticness(x):
    try:
        track_features = get_track_features(x)
        acousticness = track_features[0]['acousticness']
        return acousticness
    except:
        return None

def get_danceability(x):
    try:
        track_features = get_track_features(x)
        danceability = track_features[0]['danceability']
        return danceability
    except:
        return None

def get_energy(x):
    try:
        track_features = get_track_features(x)
        energy = track_features[0]['energy']
        return energy
    except:
        return None

def get_instrumentalness(x):
    try:
        track_features = get_track_features(x)
        instrumentalness = track_features[0]['instrumentalness']
        return instrumentalness
    except:
        return None

def get_liveness(x):
    try:
        track_features = get_track_features(x)
        liveness = track_features[0]['liveness']
        return liveness
    except:
        return None

def get_loudness(x):
    try:
        track_features = get_track_features(x)
        loudness = track_features[0]['loudness']
        return loudness
    except:
        return None


def get_speechiness(x):
    try:
        track_features = get_track_features(x)
        speechiness = track_features[0]['speechiness']
        return speechiness
    except:
        return None

def get_tempo(x):
    try:
        track_features = get_track_features(x)
        tempo = track_features[0]['tempo']
        return tempo
    except:
        return None

def get_time_signature(x):
    try:
        track_features = get_track_features(x)
        time_signature = track_features[0]['time_signature']
        return time_signature
    except:
        return None

def main():
    temp_df['album'] = streaming_df_final['track_id'].apply(get_album)
    temp_df.to_csv('album.csv')

    temp_df['release_date'] = streaming_df_final['track_id'].apply(get_release_date)
    temp_df.to_csv('release_date.csv')

    temp_df['track_length'] = streaming_df_final['track_id'].apply(get_track_length)
    temp_df.to_csv('track_length.csv')

    temp_df['popularity'] = streaming_df_final['track_id'].apply(get_popularity)
    temp_df.to_csv('popularity.csv')

    temp_df['acousticness'] = streaming_df_final['track_id'].apply(get_acousticness)
    temp_df.to_csv('acousticness.csv')

    temp_df['danceability'] = streaming_df_final['track_id'].apply(get_danceability)
    temp_df.to_csv('danceability.csv')

    temp_df['energy'] = streaming_df_final['track_id'].apply(get_energy)
    temp_df.to_csv('energy.csv')

    temp_df['instrumentalness'] = streaming_df_final['track_id'].apply(get_instrumentalness)
    temp_df.to_csv('instrumentalness.csv')

    temp_df['liveness'] = streaming_df_final['track_id'].apply(get_liveness)
    temp_df.to_csv('liveness.csv')

    temp_df['loudness'] = streaming_df_final['track_id'].apply(get_loudness)
    temp_df.to_csv('loudness.csv')

    temp_df['speechiness'] = streaming_df_final['track_id'].apply(get_speechiness)
    temp_df.to_csv('speechiness.csv')

    temp_df['tempo'] = streaming_df_final['track_id'].apply(get_tempo)
    temp_df.to_csv('tempo.csv')
    
    temp_df['time_signature'] = streaming_df_final['track_id'].apply(get_time_signature)
    temp_df.to_csv('time_signature.csv')
    
    streaming_df_final.to_csv('processed_streaming_history.csv')


main()