# CS 222 - Group 73
# Project: Music Genre Classifier

# Members:
David, Jacob, Max, Daniel

# Roles:
- David - Manager
- Jacob - Front-End
- Max & Daniel - Back-End

# Overview:
- A website that takes in a .wav audio file and tells the user what genre of music it is.
- It uses recurrent neural networks (RNN) in the backend to build a model that predicts the genre of input music.

# Technical Architecture:
- We took a dataset of 1000 audio files (100 per genre) and converted each audio clip into an MFCC matrix.
- We split the songs into training and test sets and trained our model using a recurrent neural network.
- From the website (front-end), users can input a .wav audio file which is then sent to the model in the backend.
- The model predicts the genre, and then sends the result back to the user interface.

# Usage Instructions:

- To run the project locally on your machine:
- Git clone this repository onto your local machine.
- To run the front-end:
- From the root directory, cd into music-web.
- Then cd into client.
- Run "npm install" in the terminal.
- Run "npm start" in the terminal.
- You should now be on the website if you open localhost:3000 in your browser.
- To run the back-end:
- From the root directory, cd into music-web.
- Then cd into flask-server.
- Run "python server.py" in the terminal.
- Now, you can put in .wav files into the website and receive the genre.

# Technologies:
- Front-End: React, JavaScript, HTML/CSS, DaisyUI.
- Back-End: Flask, Python, TensorFlow/Keras, NumPy, Librosa.
