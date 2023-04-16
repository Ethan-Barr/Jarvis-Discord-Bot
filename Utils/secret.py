import json
import os

with open(r'Utils/config.json','r') as f:
    config = json.load(f)

token = config['token']
prefix = config['prefix']
name = config['name']
carterAPI = config['carterKey']

print(token, prefix, carterAPI)