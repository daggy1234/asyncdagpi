import asyncio
import logging
import time
from typing import Dict

import aiohttp
from ratelimiter import RateLimiter

from . import errors
from .image import Image

log = logging.getLogger(__name__)

error_dict = {
    400: errors.ParameterError("Parameters passed were incorrect"),
    413: errors.FileTooLarge("The Image Passed is too large"),
    422: errors.ApiError("API was unable to manipulate the Image"),
    500: errors.ApiError("Internal Server Error"),
    429: errors.RateLimited("You are being Rate_limited"),
    403: errors.Unauthorised("403 Returned"),
}


class HTTP:
    """
        HTTP Client
        -----------
        Represents an HTTP client sending HTTP requests to the top.gg API.
            .. _aiohttp session:
    https://aiohttp.readthedocs.io/en/stable/client_reference.html#client-session
            Parameters
            ----------
            token: :class:`str`
                A dagpi Token from https://dagpi.xyz
            **kwargs:
                **session : Optional[aiohttp session]
                    The session used to request to the API
                **loop: Optional[asyncio loop]
                    The asyncio loop to use
    """

    __slots__ = ("client", "base_url", "token", "loop", "user_agent", "ratelimiter")

    def __init__(self, token: str, **kwargs):
        self.base_url = "https://api.dagpi.xyz"
        self.token = token
        self.loop = loop = kwargs.get("loop", None) or asyncio.get_event_loop()
        self.client = kwargs.get("session") or aiohttp.ClientSession(loop=loop)
        self.ratelimiter = RateLimiter(max_calls=60, period=60, callback=limited)
        self.user_agent = "AsyncDagpi v{__version__} Python/Python/ \
        {sys.version_info[0]}.{sys.version_info[1]} aiohttp/{2}"

    async def data_request(self, url: str, **kwargs) -> Dict:
        """

        url: :class:`str`
            url to request
        :return: :class:`Dict`
            Python Dictionary
        """
        async with self.ratelimiter:
            if not self.token:
                raise errors.Unauthorised("Please Provide a dagpi token")

            headers = {"Authorization": self.token, "User-Agent": self.user_agent}

            request_url = self.base_url + "/data/" + url
            if kwargs.get("image"):
                request_url = self.base_url + "/image/"
            async with self.client.get(request_url, headers=headers) as resp:
                if 300 >= resp.status >= 200:
                    if resp.headers["Content-Type"] == "application/json":
                        js = await resp.json()
                        return js

                    else:
                        raise errors.ApiError(
                            f"{resp.status}. \
                        Request was great but Dagpi did not send a JSON"
                        )
                else:
                    try:
                        error = error_dict[resp.status]
                        raise error
                    except KeyError:
                        raise errors.ApiError("Unknown API Error Occurred")

    async def image_request(self, url: str, params: dict) -> Image:
        """

        url: :class:`str`
            A string containing the URL
        params: :class:`Dict`
            A dictionary of the URL parameters
        :return: :class:`asyncdagpi.Image`
            Asyncdagpi Image Object
        """

        async with self.ratelimiter:
            if not self.token:
                raise errors.Unauthorised("Please Provide a dagpi token")

            headers = {"Authorization": self.token, "User-Agent": self.user_agent}

            request_url = self.base_url + "/image" + url
            async with self.client.get(
                request_url, headers=headers, params=params
            ) as resp:
                resp_time = resp.headers["X-Process-Time"][:5]
                print(
                    "GET {} has returned {} taking {}s".format(
                        resp.url, resp.status, resp_time
                    )
                )
                if 300 >= resp.status >= 200:
                    if resp.headers["Content-Type"] in ["image/png", "image/gif"]:
                        form = resp.headers["Content-Type"].replace("image/", "")

                        raw_byte = await resp.read()
                        return Image(raw_byte, form, resp_time, params.get("url"))

                    else:
                        raise errors.ApiError(
                            f"{resp.status}. \
                    Request was great but Dagpi did not send an Image back"
                        )
                else:
                    try:
                        error = error_dict[resp.status]
                        raise error
                    except KeyError:
                        js = await resp.json()
                        if resp.status == 415:
                            raise errors.ImageUnaccesible(415, js["message"])
                        elif resp.status == 400:
                            raise errors.ParameterError(400, js["message"])
                        else:
                            raise errors.ApiError("Unknown API Error Occurred")

    async def close(self):
        await self.client.close()


def limited(until):
    """Handles Rate limiting Messages"""
    duration = int(round(until - time.time()))
    log.warning("Rate limited, Retrying in {:d} seconds".format(duration))
