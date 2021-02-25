import re
import time
from typing import Dict

from .errors import BadUrl, InvalidFeature
from .http import HTTP
from .image import Image
from .image_features import ImageFeatures
from .objects import WTP, PickupLine, Logo, Headline

url_regex = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]| " \
            r"(?:%[0-9a-fA-F][0-9a-fA-F]))+"


class Client:
    """
    Initialisation
    ~~~~~~~~~~~~~~


    :param token: Your Dagpi Api token
    :param logging: Wether or not to log api requests (default True)
    :param **kwargs: Extra arguments you may pass this can include

        * loop: an asyncio event loop for the asyncdagpi to use
        * session: an aiohttp ClientSession for dagpi to use


    This will initialise an AsyncDagpiClient that you can use for making
    dagpi requests.
    """

    def __init__(self, token: str, logging: bool = True, **kwargs):

        self.token = token
        self.logging = logging
        self.session = kwargs.get("session")
        self.loop = kwargs.get("loop")
        self.http = HTTP(self.token, logging, loop=self.loop,
                         session=self.session)

    @staticmethod
    def url_test(url: str):
        if not isinstance(url, str):
            raise BadUrl("URL is not a String")

        regex = re.compile(
            url_regex,
            re.IGNORECASE)
        match = re.match(regex, url)
        if not match:
            raise BadUrl("URL did not pass Regex")

    async def image_process(self, feature: ImageFeatures, url: str, **kwargs) \
            -> Image:
        """
        feature: :class:`ImageFeature`
            a dagpi ImageFeature class

        url: :class:`str`
            the Url for the Image Passed

        kwargs:
            based on the Docs for your Feature chose the right
            extra kwargs like `text` or `username`


        :return: :class:`asyncdagpi.Image`
            Asyncdagpi Image Object
        """
        if not isinstance(feature, ImageFeatures):
            raise InvalidFeature("{} does not exist".format(str(feature)))
        self.url_test(url)
        dark = kwargs.get("dark")
        if dark is not None:
            kwargs["dark"] = str(dark)
        params = {"url": url, **kwargs}
        return await self.http.image_request(feature.value, params=params)

    async def wtp(self) -> WTP:
        """
        get a WTP data object
        :returns: :class:`asyncdagpi.WTP`
        """
        raw_data = await self.http.data_request("wtp")
        return WTP(raw_data)

    async def logo(self) -> Logo:
        """
        get a Logo data object
        :returns: :class:`asyncdagpi.Logo`
        """
        raw_data = await self.http.data_request("logo")
        return Logo(raw_data)

    async def roast(self) -> str:
        """
        Returns a string with a Roast
        :returns: :class:`str`
        """
        obj = await self.http.data_request("roast")
        return obj["roast"]

    async def yomama(self) -> str:
        """
        Returns a YoMama Joke String
        :returns: :class:`str`
        """
        obj = await self.http.data_request("yomama")
        return obj["description"]

    async def joke(self) -> str:
        """
        Gets a Funny Joke
        :returns: :class:`str`
        """
        obj = await self.http.data_request("joke")
        return obj["joke"]

    async def fact(self) -> str:
        """
        Gets a Fun fact
        :returns: :class:`str`
        """
        obj = await self.http.data_request("fact")
        return obj["fact"]

    async def eight_ball(self) -> str:
        """
        Gets an 8ball response
        :returns: :class:`str`
        """
        obj = await self.http.data_request("8ball")
        return obj["response"]

    async def pickup_line(self) -> PickupLine:
        """
        Get a PickupLine
        """

        return PickupLine(await self.http.data_request("pickupline"))

    async def headline(self) -> Headline:
        """
        Get a PickupLine
        """

        return Headline(await self.http.data_request("headline"))

    async def waifu(self) -> Dict:
        """
        Get a Random Anime Waifu.
        Does not return a model due to sheer complexity and impracticality.
        """
        return await self.http.data_request("waifu")

    async def data_ping(self) -> float:
        """
        Returns a float with the Data API's ping
        """
        start = time.perf_counter()
        await self.http.data_request("wtp")
        end = time.perf_counter()
        return (end - start)

    async def image_ping(self) -> float:
        """
        Returns a float with the Image API's ping
        """
        start = time.perf_counter()
        await self.http.data_request("/", image=True)
        end = time.perf_counter()
        return (end - start)

    async def close(self):
        """
        Shuts down the asyncdagpi Client
        """
        await self.http.close()
