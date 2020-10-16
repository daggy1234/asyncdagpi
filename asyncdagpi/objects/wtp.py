import json
from typing import Dict


class WTP(object):

    def __init__(self, json: Dict):
        mon = json.get("Data")
        self.dict = json
        self.abilities = mon.get("abilities")
        self.ascii = mon.get("ascii")
        self.height = mon.get("height")
        self.id = mon.get("id")
        self.link = mon.get("link")
        self.name = mon.get("name")
        self.type = mon.get("type")
        self.weight = mon.get("weight")
        self.question = json.get("question")
        self.answer = json.get("answer")

    def __str__(self) -> str:
        """Returns a string of the data"""
        return json.dumps(self.dict)

    def raw_data(self) -> Dict:
        """Dictionary with Raw Data"""
        return self.dict
