import os
import requests
import json
from dotenv import load_dotenv
from textblob import TextBlob

load_dotenv()
access_key = os.getenv('ACCESS_KEY')
image_api = 'https://api.unsplash.com/'

# The text to analyze
filename = 'data/chamounix_synopsis.txt'
file = open(filename, 'r')
text = file.read()

# blob = TextBlob(text)
# print(blob.tags)

payload = {'client_id': access_key, 'query': 'clouds', 'page': '1', 'per_page': '1'}
r = requests.get(image_api+'search/photos', params=payload)
resp = r.json()
# print(json.dumps(resp, indent=1))
print(resp['results'][0]['urls']['raw'])