from dataclasses import dataclass
from typing import Self
from json import JSONDecodeError

@dataclass
class Data(object):
    x:int
    y:int
    z:int
    name:str
    sub_values:list #risque de sécurité ici, pensez a vérifier vos types ;)
    def __init__(self) -> None:
        self.x =0
        self.y =1
        self.z =0
        self.name = "foo"
        self.sub_values=[]

    @staticmethod
    def init_with_values(x =0,y=1,z=0,name="foo",sub_values=[])-> Self:
        data = Data()
        data.x = x
        data.y = y
        data.z = z
        data.name = name
        data.subvalues = sub_values
        return data

    @staticmethod
    def from_json(json: dict)-> Self:
        if not isinstance(json["x"],int):
            raise JSONDecodeError("invalid JSON passed to decoder")
        if not isinstance(json["y"],int):
            raise JSONDecodeError("invalid JSON passed to decoder")
        if not isinstance(json["z"],int):
            raise JSONDecodeError("invalid JSON passed to decoder")
        if not isinstance(json["name"],str):
            raise JSONDecodeError("invalid JSON passed to decoder")
        if not isinstance(json["sub_values"],list):
            raise JSONDecodeError("invalid JSON passed to decoder")
        return Data.init_with_values(json["x"],json["y"],json["z"],json["name"],json["sub_values"])
