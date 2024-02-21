import json
from Data import Data
with open("data.json","r") as file:
    data = json.loads(file.read(),object_hook=Data.from_json)
print(data)