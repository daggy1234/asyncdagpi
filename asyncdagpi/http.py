from asyncdagpi.objects import Ratelimits
import asyncio
from asyncio.events import AbstractEventLoop
import logging
from typing import Dict, Optional, Any

import aiohttp

from aiohttp import __version__ as aiov
from aiohttp.client import ClientSession

from . import errors
import sys
from .image import Image

error_dict: Dict[int, errors.AsyncDagpiHttpException] = {
    400: errors.ParameterError("Parameters passed were incorrect"),
    413: errors.FileTooLarge("The Image Passed is too large"),
    500: errors.ApiError("Internal Server Error"),
    429: errors.RateLimited("You are being Rate_limited"),
    403: errors.Unauthorised("403 Returned")
}


log: logging.Logger = logging.getLogger(__name__)


class HTTP:

    """
    HTTP Client
    -----------
    Represents an HTTP client sending HTTP requests to the dagpi API.
        .. _aiohttp session:
https://aiohttp.readthedocs.io/en/stable/client_reference.html#client-session
        Parameters
        ----------
        :param token: :class:`str`
            A dagpi Token from https://dagpi.xyz
        *args:
            **session : Optional[aiohttp session]
                The session used to request to the API
            **loop: Optional[asyncio loop]
                The asyncio loop to use
    """

    __slots__ = ("client", "base_url", "token", "loop",
                 "user_agent", "logging", "ratelimits")

    def __init__(
        self,
        token: str,
        session: Optional[aiohttp.ClientSession],
        loop: Optional[asyncio.AbstractEventLoop]
    ):
        """
        Initialise the dagpi http client
        """
        self.base_url: str = "https://api.dagpi.xyz"
        self.token: str = token
        self.loop: AbstractEventLoop = loop or asyncio.get_event_loop()
        self.client: ClientSession = session or aiohttp.ClientSession(loop=loop)
        self.ratelimits: Ratelimits = Ratelimits(None, None, None)
        from asyncdagpi import __version__
        self.user_agent: str = f"AsyncDagpi v{__version__} Python/{sys.version_info[0]}.{sys.version_info[1]} \
            aiohttp/{aiov}"

    async def data_request(self, url: str, *, image: Optional[bool] = None) -> Dict[str, Any]:
        """

        url: :class:`str`
            url to request
        :return: :class:`Dict`
            Python Dictionary
        """

        if not self.token:
            raise errors.Unauthorised("Please Provide a dagpi token")

        headers = {
            "Authorization": self.token,
            'User-Agent': self.user_agent
        }

        request_url = self.base_url + "/data/" + url
        if image:
            request_url = self.base_url + "/image/"
        async with self.client.get(request_url, headers=headers) as resp:
            self.ratelimits = Ratelimits.from_dict(resp.headers)
            if 300 >= resp.status >= 200:
                if resp.headers["Content-Type"] != "application/json":
                    raise errors.ApiError(f"{resp.status}. \
                    Request was great but Dagpi did not send a JSON")
                js: Dict[str, Any] = await resp.json()
                return js

            else:
                try:
                    error = error_dict[resp.status]
                    raise error
                except KeyError:
                    raise errors.ApiError("Unknown API Error Occurred")

    async def image_request(self, url: str, params: Dict[str, str]) -> Image:
        """

        url: :class:`str`
            A string containing the URL
        params: :class:`Dict`
            A dictionary of the URL parameters
        :return: :class:`asyncdagpi.Image`
            Asyncdagpi Image Object
        """

        if not self.token:
            raise errors.Unauthorised("Please Provide a dagpi token")

        headers = {
            "Authorization": self.token,
            'User-Agent': self.user_agent
        }

        request_url = self.base_url + "/image" + url
        async with self.client.get(request_url, headers=headers,
                                   params=params) as resp:
            self.ratelimits = Ratelimits.from_dict(resp.headers)
            if 300 >= resp.status >= 200:
                if resp.headers["Content-Type"].lower() not in [
                    "image/png",
                    "image/gif",
                ]:
                    raise errors.ApiError(f"{resp.status}. \
                Request was great but Dagpi did not send an Image back")
                form: str = resp.headers["Content-Type"].replace("image/",
                                                                 "")
                resp_time = resp.headers["X-Process-Time"][:5]
                raw_byte = await resp.read()
                log.info(
                    f'[Dagpi Image] GET {resp.url} has returned {resp.status}')
                return Image(raw_byte, form, resp_time,
                             params["url"])

            else:
                try:
                    error = error_dict[resp.status]
                    raise error
                except KeyError:
                    js = await resp.json()
                    if resp.status == 415:
                        raise errors.ImageUnaccesible(415, js["message"])
                    elif resp.status == 400:
                        raise errors.ParameterError(js["message"])
                    elif resp.status == 422:
                        try:
                            mstr = ""
                            for val in js["detail"]:
                                base = f'{val["loc"][1]} is {val["type"]}'
                                mstr += (base + "\t")
                            raise errors.ParameterError(mstr)
                        except KeyError:
                            raise errors.ApiError(
                                "API was unable to manipulate the Image")
                    else:
                        raise errors.ApiError("Unknown API Error Occurred")
                finally:
                    log.error(f'[Dagpi Image] GET {resp.url} has returned {resp.status}')

    async def close(self) -> None:
        await self.client.close()
