import re
import time
from typing import Dict, Optional, Any

from .errors import BadUrl, InvalidFeature
from .http import HTTP
from .image import Image
from .image_features import ImageFeatures
from .objects import Captcha, Typeracer, WTP, PickupLine, Logo, Headline, Ratelimits
from aiohttp import ClientSession
from asyncio import AbstractEventLoop


url_regex: str = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]| " \
    r"(?:%[0-9a-fA-F][0-9a-fA-F]))+"


class Client:

    """
    Initialisation
    ~~~~~~~~~~~~~~


    :param token: Your Dagpi Api token
    :param **kwargs: Extra arguments you may pass this can include

        * loop: an asyncio event loop for the asyncdagpi to use
        * session: an aiohttp ClientSession for dagpi to use


    This will initialise an AsyncDagpiClient that you can use for making
    dagpi requests.
    """

    def __init__(
        self,
        token: str,
        *,
        session: Optional[ClientSession] = None,
        loop: Optional[AbstractEventLoop] = None
    ):

        self.token: str = token
        self.session: Optional[ClientSession] = session
        self.loop: Optional[AbstractEventLoop] = loop
        self.http: HTTP = HTTP(self.token, loop=self.loop,
                               session=self.session)

    @staticmethod
    def url_test(url: str) -> None:
        if not isinstance(url, str):
            raise BadUrl("URL is not a String")

        regex = re.compile(
            url_regex,
            re.IGNORECASE)
        match = re.match(regex, url)
        if not match:
            raise BadUrl("URL did not pass Regex")

    @property
    def ratelimits(self) -> Ratelimits:
        """Get ratelimits for your client
        """
        return self.http.ratelimits

    async def image_process(
        self,
        feature: ImageFeatures,
        url: str,
        **kwargs: Any) \
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
            raise InvalidFeature(f"{feature} does not exist")
        self.url_test(url)
        dark = kwargs.get("dark")
        if dark is not None:
            kwargs["dark"] = str(dark)
        params: Dict[str, str] = {"url": url, **kwargs}
        return await self.http.image_request(feature.value, params=params)

    async def special_image_process(self, url: str) \
            -> Image:
        """

        url: :class:`str`
            the Url for the Image Passed

        :return: :class:`asyncdagpi.Image`
            Asyncdagpi Image Object
        """
        self.url_test(url)
        params = {"url": url}
        return await self.http.image_request("/special/", params=params)

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

    async def captcha(self) -> Captcha:
        """
        Get a captcha
        """

        return Captcha(await self.http.data_request("captcha"))

    async def typeracer(self) -> Typeracer:
        """
        Get a sentence on an image
        """

        return Typeracer(await self.http.data_request("typeracer"))

    async def waifu(self) -> Dict[str, Any]:
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

    async def close(self) -> None:
        """
        Shuts down the asyncdagpi Client
        """
        await self.http.close()
