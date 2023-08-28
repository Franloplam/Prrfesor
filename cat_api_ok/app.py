from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse, HTMLResponse
from get_features import get_features
import os
import numpy as np
import librosa
import tensorflow as tf
import streamlit as st

app = FastAPI()

class Cat_Class:
    def __init__(self, model_path):
        self.model = tf.keras.models.load_model(model_path)

    def save_audio(self, file):
        with open(file.filename, "wb") as f:
            f.write(file.file.read())
        result = self.prediction(file.filename)
        os.remove(file.filename)  # Eliminar el archivo después de usarlo
        return result

    def prediction(self, audio_file):
        results = []
        result = ""
        try:
            features = get_features(audio_file)
            features = np.expand_dims(features, axis=0)
            features = np.expand_dims(features, axis=2)
            predict = self.model.predict(features)
            result = np.argmax(predict, axis=1)
            results.append(result)
            if results[0][0] == 0:
                result = "Your cat wants to be brushed"
            elif results[0][0] == 1:
                result = "Your cat feels isolated"
            elif results[0][0] == 2:
                result = "Your cat is hungry"
        except (FileNotFoundError, librosa.LibrosaError):
            result = f"Error loading file: {audio_file}"
        return result

@app.post("/predict/")
async def predict_post(file: UploadFile = File(...)):
    if not file.filename.endswith(".wav"):
        return JSONResponse(content="File must be in WAV format", status_code=400)

 #local_model_path = "/home/fll_data_bata/code/Franloplam/DB Gatos/trained_model.h5"
    local_model_path = "trained_model.h5"
    cat_init = Cat_Class(local_model_path)

    resultado = cat_init.save_audio(file)
    return {"result": resultado}

@app.get("/predict/")
async def predict_get():
    content = """
    <html>
    <body>
    <form action="/predict/" enctype="multipart/form-data" method="post">
        <input type="file" name="file">
        <input type="submit" value="Predict">
    </form>
    </body>
    </html>
    """
    return HTMLResponse(content=content)
