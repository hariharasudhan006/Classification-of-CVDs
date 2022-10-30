import os
import numpy as np
from flask import Flask, request, render_template, send_from_directory
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

CVDs = [
    'Left Bundle Branch Block',
    'Normal',
    'Premature Atrial Contraction',
    'Premature Ventricular Contractions',
    'Right Bundle Branch Block',
    'Ventricular Fibrillation'
]

app = Flask(__name__)


@app.route("/")
@app.route("/index.html")
def home():
    return render_template("index.html")


@app.route("/info.html")
def info():
    return render_template("info.html")


def predict_cvd():
    pass


@app.route("/predict.html", methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        request.files['image'].save("ecg.png")
        img = np.expand_dims(image.img_to_array(
            image.load_img("ecg.png", target_size=(64, 64), color_mode="grayscale")), axis=0)
        model = load_model("model_30_oct_22.h5")
        prediction = model.predict(img)
        print("Prediction:", prediction)
        return CVDs[list(prediction[0]).index(1)]
    return render_template("predict.html")


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == "__main__":
    app.run(debug=True)
