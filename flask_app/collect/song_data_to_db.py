import pandas as pd
import sqlite3

df = pd.read_csv("flask_app/song_data.csv", encoding = "UTF-8")

con = sqlite3.connect("flask_app/song_data.db")

df.to_sql('song_data', con)