from flask import Flask, render_template, request
from PIL import Image
import tensorflow as tf
import numpy as np
import cv2 
import os

app = Flask(__name__, template_folder="templates")
model = tf.keras.models.load_model("cheetahjaguarclassifier.keras")

@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")
    elif request.method == 'POST':
        if 'image' not in request.files:
            return "No images"
        file = request.files['image']
        if file.filename == '':
            return "No file"
        
        temp_path = "temp_upload.jpg"
        file.save(temp_path)
        
        test_img1 = cv2.imread(temp_path)
        test_img1 = cv2.resize(test_img1, (256, 256))

        raw_pred = model.predict(np.expand_dims(test_img1/255,0))
        result = "Cheetah" if raw_pred[0][0] < 0.5 else "Jaguar"

        if os.path.exists(temp_path):
            os.remove(temp_path)
        
        return render_template("result.html", result=result)
app.run(host="0.0.0.0", port=5555, debug=True)