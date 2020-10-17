import json
from typing import Dict


class BaseDagpiObject:
    def __str__(self) -> str:
        """Returns a string of the data"""
        return json.dumps(self.dict)

    def raw_data(self) -> Dict:
        """Dictionary with Raw Data"""
        return self.dict


class Logo(BaseDagpiObject):

    def __init__(self, data: Dict):
        self.dict = data
        self.question = data.get("question")
        self.answer = data.get("answer")
        self.brand = data.get("brand")
        self.clue = data.get("clue")
        self.easy = data.get("easy")
        self.hint = data.get("hint")
        self.wiki_url = data.get("wiki_url")


class PickupLine(BaseDagpiObject):
    """
    A Dagpi PickupLine

    .. container:: Attributes

        **Attributes**

        dict: :class:`Dict`
            Dictionary with raw data (same returned by raw_data)
        category: :class:`str`
            String containing Type of Pickup Line
        line: :class:`str`
            String Containing Pickup Line
    """

    def __init__(self, data: Dict):
        self.dict = data
        self.category = data.get("category")
        self.line = data.get("joke")


class WTP(BaseDagpiObject):

    def __init__(self, data: Dict):
        mon = data.get("Data")
        self.dict = data
        self.abilities = mon.get("abilities")
        self.ascii = mon.get("ascii")
        self.height = mon.get("height")
        self.id = mon.get("id")
        self.link = mon.get("link")
        self.name = mon.get("name")
        self.type = mon.get("type")
        self.weight = mon.get("weight")
        self.question = data.get("question")
        self.answer = data.get("answer")
