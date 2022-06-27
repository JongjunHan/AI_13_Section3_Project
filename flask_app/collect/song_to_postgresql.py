import psycopg2
import csv

connection = psycopg2.connect(host = 'localhost', database = 'postgres', user = 'postgres', password = 'jongjun100', port = 5432)

cur = connection.cursor()

cur.execute("""CREATE TABLE song_data (
                id INT PRIMARY KEY,
				song_name VARCHAR(255),
                song_popularity INT,
                song_duration_ms INT,
                acousticness FLOAT,
                danceability FLOAT,
                energy FLOAT,
                instrumentalness FLOAT,
                key INT,
                liveness FLOAT,
                loudness FLOAT,
                audio_mode INT,
                speechiness FLOAT,
                tempo FLOAT,
                time_signature INT,
                audio_valence FLOAT);
			""")

cur.execute("""CREATE TABLE song_info (
                id INT PRIMARY KEY,
				song_name VARCHAR(255),
                artist_name VARCHAR(255),
                album_names VARCHAR(255),
                playlist VARCHAR(255));
			""")

with open('song_data.csv', encoding = 'UTF-8') as csvfile:
    myReader = csv.reader(csvfile)
    next(myReader)

    enu = enumerate(myReader)
    total_row = len(open('song_data.csv', encoding = 'UTF-8').readlines())

    for idx, row in enu:
        cur.execute(f'INSERT INTO song_data VALUES ({idx}, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', row)

        if idx % 1000 == 0:
            connection.commit()
            print(f'{idx}/{total_row} progressed')

with open('song_info.csv', encoding = 'UTF-8') as csvfile:
    myReader = csv.reader(csvfile)
    next(myReader)

    enu = enumerate(myReader)
    total_row = len(open('song_info.csv', encoding = 'UTF-8').readlines())

    for idx, row in enu:
        cur.execute(f'INSERT INTO song_info VALUES ({idx}, %s, %s, %s, %s)', row)

        if idx % 1000 == 0:
            connection.commit()
            print(f'{idx}/{total_row} progressed')

connection.commit()
print(f'{total_row}/{total_row} progressed')

connection.close()