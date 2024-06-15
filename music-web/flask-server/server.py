
from io import BytesIO
from flask import jsonify, request, Flask, render_template, redirect
app = Flask(__name__)
from flask_cors import CORS
CORS(app)
from tensorflow import keras
import librosa
import sys
import numpy as np
import math
import librosa.display

sys.path.append('../../')

from genre_classifier import load_data, plot_history, prepare_dataset, build_model, actual_predict

# get saved ML model
model = keras.models.load_model('../../model.h5')

# import from two directories up
import sys
sys.path.append('../../')

import os

app.config['UPLOAD_FOLDER'] = 'uploads'

"""Handles the upload of a file."""
@app.route('/upload_file', methods=['POST'])
def upload_file():
    d = {} # 1 - success, 0 - failure
    try:
        print("uploading file...")
        file = request.files['file_from_react']
        filename = file.filename
        print(f"Uploading file {filename}")
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        uploaded_file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        print(uploaded_file_path)

        # check duration:
        audio_duration = (librosa.get_duration(filename=uploaded_file_path))

        if audio_duration < 30:
            print("Audio too short")
            d['success'] = 0
            d['message'] = "Audio too short"
            return jsonify(result="audio file must be longer than 30 seconds")
        signal, sr = librosa.load(uploaded_file_path, sr=22050)
        prediction_res = (actual_predict(model, np.array(get_mat(signal, sr))))
        d['status'] = 1
        return jsonify(result=prediction_res)

    except Exception as error:
        print(f"Couldn't upload file: {error}.")
        d['status'] = 0

    return jsonify(d)

def get_mat(signal, sr):
    SAMPLE_RATE = 22050
    DURATION = 30
    SAMPLES_PER_TRACK = SAMPLE_RATE * DURATION
    num_samples_per_segment = int(SAMPLES_PER_TRACK / 6)
    # expected_num_mfcc_vectors_per_segment = math.ceil(num_samples_per_segment / 512)
    # print(expected_num_mfcc_vectors_per_segment) # 216
    expected_num_mfcc_vectors_per_segment = 216

    comb = []
    for s in range(6) :
        start_sample = num_samples_per_segment * s
        finish_sample = start_sample + num_samples_per_segment

        mfcc = librosa.feature.mfcc(y = signal[start_sample:finish_sample], sr = sr, n_fft=2048, n_mfcc=13, hop_length=512)
        mfcc = mfcc.T
        if len(mfcc) == expected_num_mfcc_vectors_per_segment:
            comb.append(mfcc.tolist())
        
    # print(comb)
    return comb

# save for a passed song:
# def save_mfcc(file_name, n_mfcc=13, n_fft=2048, hop_length=512):
#     # sample_rate = 22050
#     # duration = 30
#     # samples_per_track = sample_rate * duration
#     # num_samples_per_segment = int(samples_per_track / num_segments)

#     file_path = os.path.join(dirpath, f)
#     mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
#     mfccs = mfccs.T
#     print(mfccs)
#     return 3

if __name__ == '__main__':
    # run in development mode
    app.run(debug=True)