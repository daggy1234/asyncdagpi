import json
from typing import Dict


class PickupLine(object):
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

    def __init__(self, json: Dict):
        self.dict = json
        self.category = json.get("category")
        self.line = json.get("joke")

    def __str__(self) -> str:
        """Returns a string of the data"""
        return json.dumps(self.dict)

    def raw_data(self) -> Dict:
        """Dictionary with Raw Data"""
        return self.dict
