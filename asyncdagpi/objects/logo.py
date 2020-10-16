import json
from typing import Dict


class Logo(object):

    def __init__(self, json: Dict):
        self.dict = json
        self.question = json.get("question")
        self.answer = json.get("answer")
        self.brand = json.get("brand")
        self.clue = json.get("clue")
        self.easy = json.get("easy")
        self.hint = json.get("hint")
        self.wiki_url = json.get("wiki_url")

    def __str__(self) -> str:
        """Returns a string of the data"""
        return json.dumps(self.dict)

    def raw_data(self) -> Dict:
        """Dictionary with Raw Data"""
        return self.dict
