import json
from pymongo import MongoClient
import os

username = os.getenv('MONGODB_USER_COMMANDS_WRITE')
password = os.getenv('MONGODB_PASSWORD_COMMANDS_WRITE')
host_name = os.getenv('HOST_NAME')

client = MongoClient(f'mongodb://{username}:{password}@{host_name}/')

db = client['Security_Audit']
collection = db['Commands']

with open('own_commands.json') as file:
    data = json.load(file)

collection.insert_many(data)

client.close()
