from flask import Flask, render_template, request
import pickle
import numpy as np
from sklearn.pipeline import make_pipeline
import pandas as pd

df = pd.read_csv('./flask_app/song_data.csv', encoding = 'UTF-8')

def create_app():
    popularitify = Flask(__name__)

    with open('flask_app/modeling/model.pkl', 'rb') as pickel_file:
        model = pickle.load(pickel_file)
        
    @popularitify.route('/')
    def home():
        return render_template('home.html')

    @popularitify.route('/song-data', methods = ['GET', 'POST'])
    def data():
        return render_template('song-data.html')

    @popularitify.route('/dashboard', methods = ['GET','POST'])
    def dashboard():
        return render_template('dashboard.html')
    
    @popularitify.route('/information', methods = ['GET','POST'])
    def info():
        return render_template('info.html')
        
    @popularitify.route('/song-popularity', methods = ['POST'])
    def modeling():
        acousticness = request.form['acousticness']
        danceability = request.form['danceability']
        energy = request.form['energy']
        audio_mode = request.form['audio_mode']
        speechiness = request.form['speechiness']
        tempo = request.form['tempo']
        song_duration = request.form['song_duration']

        song_info = pd.DataFrame(columns = ['acousticness', 'danceability', 'energy', 'audio_mode', 'speechiness', 'tempo', 'song_duration'])
        song_info['acousticness'] = [acousticness]
        song_info['danceability'] = [danceability]
        song_info['energy'] = [energy]
        song_info['audio_mode'] = [audio_mode]
        song_info['speechiness'] = [speechiness]
        song_info['tempo'] = [tempo]
        song_info['song_duration'] = [song_duration]

        pred = model.predict(song_info)[0]

        output = round(pred)

        name = df[df['song_popularity'] == output]
        real_name = name.iloc[:1, 0].tolist()

        real_output = f'점수는 {output}점 이며 비슷한 점수의 음악은 {real_name} 입니다'

        return render_template('result.html', data = real_output)

    @popularitify.errorhandler(500)
    def page_not_found(error):
        return render_template('500.html'), 500

    return popularitify

if __name__ == "__main__":
    popularitify = create_app()

    popularitify.run(debug = True)