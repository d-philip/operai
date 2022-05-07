import os
import json
import requests
from dotenv import load_dotenv
import pprint

load_dotenv()
token = os.getenv('FACE_TOKEN')
headers = {"Authorization": f"Bearer {token}"}
api_url = 'https://api-inference.huggingface.co/models/microsoft/swin-tiny-patch4-window7-224'
image_dir = 'images/'
pp = pprint.PrettyPrinter()

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.request("POST", api_url, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))

labels = {}
for folder in sorted(os.listdir(image_dir)):
    labels[folder] = []
    search_path = image_dir+folder+'/'
    
    for file in sorted(os.listdir(search_path)):
        data = query(search_path+file)
        labels[folder].append((data[0]["score"], data[0]["label"]))
        labels[folder].append((data[1]["score"], data[1]["label"]))
        labels[folder].append((data[2]["score"], data[2]["label"]))
        # print("{} | Score: {:.2f}% | Label: {}".format(file, data[0]["score"]*100, data[0]["label"]))
    
pp.pprint(labels)

# for each line of text:
#   - grab each related image and get its top 3 classification labels
#   - find most representative label (highest frequency/accuracy??)