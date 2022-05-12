import os
import requests
import json
from dotenv import load_dotenv
from textblob import TextBlob

def clean_keywords(text:str, keywords:list) -> str:
    for w in keywords:
        text = text.replace( " "+w," ")
    return text

load_dotenv()
access_key = os.getenv('ACCESS_KEY')
image_api = 'https://api.unsplash.com/'

def load_images():
    # The text to analyze
    # filename = 'data/chamounix_synopsis.txt'
    filename = 'data/hmspinafore_synopsis.txt'
    file = open(filename, 'r')
    text = file.read()
    text_list= text.split('.')

    images = []
    # blob = TextBlob(text)
    # print(blob.tags)
    
    for s in text_list:
        payload = {'client_id': access_key, 'query': s, 'page': '1', 'per_page': '1'}
        r = requests.get(image_api+'search/photos', params=payload)
        resp = r.json()
        # print(json.dumps(resp, indent=1))
        # print("\n\n"+s)
        # print(resp['results'][0]['urls']['raw'])
        images.append({'image_url': resp['results'][0]['urls']['raw'], 'text': s})
        
    return images