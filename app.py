from flask import Flask
from blob_test import load_images

app = Flask(__name__)

@app.route("/")
def hello():
    return "<p>Hello, World!</p>"

@app.route("/images")
def get_images():
    try:
        images = load_images()
        return {'images': images}
    except:
        return {'error': 'There was an error with the image retrieval.'}
    