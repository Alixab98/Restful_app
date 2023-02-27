from flask import Flask, jsonify
import numpy as np
import tensorflow as tf
import pandas as pd


app = Flask(__name__)
model = tf.keras.models.load_model('model.h5')

@app.route('/classify/<pixel_data>')
def classify(pixel_data):
    
    # Use your model to classify the image based on the pixel data
    df=pd.DataFrame([eval(pixel_data)])
    df=df/255.0
    classification = model.predict(df)
    prediction = np.argmax(classification, axis=1)
    prediction = prediction[0]
    # Return the classification as a JSON object
    return jsonify({'class': f'{prediction}'})

if __name__ == '__main__':
    app.run()
