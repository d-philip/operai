from flask import Flask, Response, request
from flask_cors import CORS
from blob_test import load_images
from google_image_crawler import image_url_crawl, image_crawl_nouns
import json
import logging

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "<p>Hello, World!</p>"

@app.route("/images/")
def get_images():
    filename=request.args['filename']
    if not filename:
        try:
            images = load_images()
            if images:
                print('Images loaded')
                return {'images': images}, 200
            else:
                print('Error loading images')
                return {'error': 'There was an error with retrieving the images.'}, 400
        except:
            logging.exception("Exception occurred.")
            print('Error loading images')
            return {'error': 'There was an error with retrieving the images.'}, 400
    else:
        try:
            image_crawl_nouns(filename=filename, num_images=2)
            json_file = 'data/image_urls.json'
            with open(json_file, 'r') as f:
                data = json.load(f)
                return data, 200
        except:
            logging.exception("Exception occurred.")
            print('Error loading test images')
            return {'error': 'There was an error with retrieving the images.'}, 400

@app.route("/images/test")
def get_test_images():
    try:
        json_file = 'data/image_urls.json'
        with open(json_file, 'r') as f:
            data = json.load(f)
            return data, 200
    except:
        logging.exception("Exception occurred.")
        print('Error loading test images')
        return {'error': 'There was an error with retrieving the test images.'}, 400

@app.route("/text")
def get_synopsis_text():
    try:
        filename=request.args['filename']
        with open(filename) as file:
            text = file.read()
            text = text.replace('*', '')
            return {'synopsis_text': text}, 200
    except:
        logging.exception("Exception occurred.")
        print('Error loading synopsis text')
        return {'error': 'There was an error with retrieving the synopsis text.'}, 400
    
if __name__ == '__main__':
    app.run(debug=True, threaded=False)