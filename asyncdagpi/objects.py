import json
from typing import Dict


class BaseDagpiObject:
    """
    Base AsyncDagpi object

        .. container:: Attributes

            **Attributes**

            dict: :class:`Dict`
    """

    def __init__(self, dictionary: Dict):
        self.dict = dictionary

    def __str__(self) -> str:
        """
        Returns a string of the data
        :returns :class:`str`
        """
        return json.dumps(self.dict)

    def raw_data(self) -> Dict:
        """
        Dictionary with Raw Data
        :returns :class:`Dict`
        """
        return self.dict


class Logo(BaseDagpiObject):
    """
        A Dagpi Logo Object. A subclass of asyncdagpi.BaseDagpiObject

        .. container:: Attributes

            **Attributes**

            dict: :class:`Dict`
                Dictionary with raw data (same returned by raw_data)
            question: :class:`str`
                String containing url of question image
            answer: :class:`str`
                String containing url of answer image
            brand: :class:`str`
                String containing name of brand
            clue: :class:`str`
                String containing hint to use for question
            easy: :class:`boolean`
                Boolean that shows wether question was easy
            hint: :class:`str`
                String containing hint
            wiki_url: :class:`str`
                String containing Wikipedia URL for brand
        """

    def __init__(self, data: Dict):
        super(Logo, self).__init__(data)
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
        super(PickupLine, self).__init__(data)
        self.dict = data
        self.category = data.get("category")
        self.line = data.get("joke")


class WTP(BaseDagpiObject):
    """
           A Dagpi PickupLine. A subclass of AsyncDagpi object

           .. container:: Attributes

               **Attributes**

               dict: :class:`Dict`
                   Dictionary with raw data (same returned by raw_data)
               abilities: :class:`List[str]`
                   A list containing the abilities the pokemon has
               ascii: :class:`str`
                   String containing ascii data of pokemons image
               height: :class:`float`
                   Float with height of pokemon
               weight: :class:`float`
                   Float with weight of pokemon
               id: :class:`int`
                   Integer with national dex id of pokemon
               link: :class:`str`
                   String containing pokemondb link for pokemon
               name: :class:`str`
                   String containing name of pokemon
               answer: :class:`str`
                   String containing url for answer image
               question: :class:`str`
                   String containing url for question image
           """

    def __init__(self, data: Dict):
        super(WTP, self).__init__(data)
        mon = data.get("Data")
        self.dict = data
        self.abilities = mon.get("abilities")
        self.ascii = mon.get("ascii")
        self.height = mon.get("height")
        self.id = int(mon.get("id"))
        self.link = mon.get("link")
        self.name = mon.get("name")
        self.type = mon.get("type")
        self.weight = mon.get("weight")
        self.question = data.get("question")
        self.answer = data.get("answer")


class Headline(BaseDagpiObject):
    """
    A Dagpi Headline

    .. container:: Attributes

        **Attributes**

        dict: :class:`Dict`
            Dictionary with raw data (same returned by raw_data)
        category: :class:`bool`
            Value stating whether headline is true or false
        headline: :class:`str`
            String Containing headline
    """

    def __init__(self, data: Dict):
        super(Headline, self).__init__(data)
        self.dict = data
        self.headline = data.get("text")
        self.fake = data.get("fake")
