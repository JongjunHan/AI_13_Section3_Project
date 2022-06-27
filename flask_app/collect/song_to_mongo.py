import csv
import os
from pymongo import MongoClient

HOST = 'cluster0.46fmd6s.mongodb.net'
USER = 'JJH'
PASSWORD = 'mongodb'
DATABASE_NAME = 'cluster0'
COLLECTION_NAME = 'spotify_song'
MONGO_URI = f"mongodb+srv://{USER}:{PASSWORD}@{HOST}/{DATABASE_NAME}?retryWrites=true&w=majority"

client = MongoClient(MONGO_URI)
database = client[DATABASE_NAME]
collection = database[COLLECTION_NAME]

collection.delete_many({})

with open('song_data.csv', encoding = "UTF-8") as song_data:
  csv_file = csv.reader(song_data)
  header = next(csv_file)

  for data in csv_file:
    dic = {
      "song_name" : str(data[0]),
      "song_popularity" : int(data[1]),
      "song_duration_ms" : int(data[2]),
      "acousticness" : float(data[3]),
      "danceability" : float(data[4]),
      "energy" : float(data[5]),
      "instrumentalness" : float(data[6]),
      "key" : int(data[7]),
      "liveness" : float(data[8]),
      "loudness" : float(data[9]),
      "audio_mode" : int(data[10]),
      "speechiness" : float(data[11]),
      "tempo" : float(data[12]),
      "time_signature" : int(data[13]),
      "audio_valence" : float(data[14])}
collection.insert_one(dic)

with open('song_info.csv', encoding = "UTF-8") as song_info:
  csv_file = csv.reader(song_info)
  header = next(csv_file)

  for data in csv_file:
    dic = {
      "song_name" : str(data[0]),
      "artist_name" : str(data[1]),
      "album_names" : str(data[2]),
      "playlist" : str(data[3])}
collection.insert_one(dic)