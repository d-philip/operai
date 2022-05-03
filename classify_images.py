import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('FACE_TOKEN')
headers = {"Authorization": f"Bearer {token}"}
api_url = 'https://api-inference.huggingface.co/models/microsoft/swin-tiny-patch4-window7-224'
image_dir = 'images/'

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.request("POST", api_url, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))

# data = query("images/000001.jpg")
# print(data[0])
for file in sorted(os.listdir(image_dir)):
    data = query(image_dir+file)
    print("{} | Score: {:.2f}% | Label: {}".format(file, data[0]["score"]*100, data[0]["label"]))