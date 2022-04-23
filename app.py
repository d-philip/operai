from flask import Flask, Response
from flask_cors import CORS
from blob_test import load_images

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "<p>Hello, World!</p>"

@app.route("/images")
def get_images():
    try:
        images = load_images()
        return {'images': images}, 200
    except:
        return {'error': 'There was an error with the image retrieval.'}, 400
    