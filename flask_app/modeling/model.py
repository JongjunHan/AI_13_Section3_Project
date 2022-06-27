import psycopg2
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestRegressor
import pickle

connection = psycopg2.connect(host = 'localhost', database = 'postgres', user = 'postgres', password = 'jongjun100', port = 5432)

cur = connection.cursor()
cur1 = connection.cursor()

cur.execute("""
            SELECT * FROM song_data;
            """)
cur1.execute("""
            SELECT * FROM song_info
            """)

result = cur.fetchall()
result1 = cur1.fetchall()

spotify_song_data = pd.DataFrame(result, columns = ['id', 'song_name', 'song_popularity', 'song_duration_ms', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'key', 'liveness', 'loudness', 'audio_mode', 'speechiness', 'tempo', 'time_signature', 'audio_valence'])
spotify_song_info = pd.DataFrame(result1, columns = ['id', 'song_name', 'artist_name', 'album_names', 'playlist'])

spotify_song_data['song_duration'] = spotify_song_data['song_duration_ms'] / 1000
spotify_song_data['acousticness'] = spotify_song_data['acousticness'] * 1000
spotify_song_data['danceability'] = spotify_song_data['danceability'] * 1000
spotify_song_data['energy'] = spotify_song_data['energy'] * 1000
spotify_song_data['speechiness'] = spotify_song_data['speechiness'] * 100 
spotify_song_data['acousticness'] = spotify_song_data['acousticness'].round(0).astype(int)
spotify_song_data['danceability'] = spotify_song_data['danceability'].round(0).astype(int)
spotify_song_data['energy'] = spotify_song_data['energy'].round(0).astype(int)
spotify_song_data['speechiness'] = spotify_song_data['speechiness'].round(0).astype(int)
spotify_song_data['tempo'] = spotify_song_data['tempo'].round(0).astype(int)
spotify_song_data['song_duration'] = spotify_song_data['song_duration'].round(0).astype(int)

spotify_song_data.drop(['id', 'song_name', 'song_duration_ms', 'instrumentalness', 'key', 'liveness', 'loudness', 'time_signature', 'audio_valence'], axis = 1, inplace = True)

# 전처리 끝

# 머신러닝 모델링 시작

X = spotify_song_data.drop('song_popularity', axis = 1)
y = spotify_song_data['song_popularity'].copy()

model = make_pipeline(
        MinMaxScaler(),
        RandomForestRegressor())
model.fit(X, y)

with open('./flask_app/modeling/model.pkl', 'wb') as pickle_file:
    pickle.dump(model, pickle_file)