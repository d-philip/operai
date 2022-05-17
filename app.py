from flask import Flask, Response
from flask_cors import CORS
from blob_test import load_images
import json

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "<p>Hello, World!</p>"

@app.route("/images")
def get_images():
    try:
        images = load_images()
        if images:
            print('Images loaded')
            return {'images': images}, 200
        else:
            print('Error loading images')
            return {'error': 'There was an error with retrieving the images.'}, 400
    except:
        print('Error loading images')
        return {'error': 'There was an error with retrieving the images.'}, 400

@app.route("/images/test")
def get_test_images():
    try:
        json_file = 'data/image_urls.json'
        with open(json_file, 'r') as f:
            data = json.load(f)
            return data, 200
    except:
        print('Error loading test images')
        return {'error': 'There was an error with retrieving the test images.'}, 400

if __name__ == '__main__':
    app.run(debug=True)