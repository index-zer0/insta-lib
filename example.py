import os
import json
from src.postImage import post

with open('auth.json') as json_file:
    data = json.load(json_file)
    user = data['user']
    password = data['password']

image = os.path.dirname(os.path.abspath(__file__)) + "\\cat.jpg"
caption = "picture of a #cat"
post(user, password, image, caption)