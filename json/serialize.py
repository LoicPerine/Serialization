import json
from Data import Data
from Encoder import Encoder

data = Data()
with open("data.json","w+",encoding="utf8") as file:
    file.write(json.dumps(data,cls=Encoder))
