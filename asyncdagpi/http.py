import asyncio
import logging
from typing import Dict

import aiohttp

from aiohttp import __version__ as aiov

from . import errors
from . import __version__
import sys
from .image import Image

log = logging.getLogger(__name__)

error_dict = {
    400: errors.ParameterError("Parameters passed were incorrect"),
    413: errors.FileTooLarge("The Image Passed is too large"),
    500: errors.ApiError("Internal Server Error"),
    429: errors.RateLimited("You are being Rate_limited"),
    403: errors.Unauthorised("403 Returned")
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
        :param token: :class:`str`
            A dagpi Token from https://dagpi.xyz
        :param logging :class:`bool`
            Wether or not to log dagpi
        **kwargs:
            **session : Optional[aiohttp session]
                The session used to request to the API
            **loop: Optional[asyncio loop]
                The asyncio loop to use
    """

    __slots__ = ("client", "base_url", "token", "loop",
                 "user_agent", "logging")

    def __init__(self, token: str, logging_enabled: bool, **kwargs):
        self.base_url = "https://api.dagpi.xyz"
        self.token = token
        self.logging = logging_enabled
        self.loop = loop = kwargs.get('loop', None) or asyncio.get_event_loop()
        self.client = kwargs.get('session') or aiohttp.ClientSession(loop=loop)
        self.user_agent = "AsyncDagpi v{0} Python/Python/ \
        {1}.{2} aiohttp/{3}".format(__version__, sys.version_info[0],
                                    sys.version_info[1], aiov)

    async def data_request(self, url: str, **kwargs) -> Dict:
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
        if kwargs.get("image"):
            request_url = self.base_url + "/image/"
        async with self.client.get(request_url, headers=headers) as resp:
            if 300 >= resp.status >= 200:
                if resp.headers["Content-Type"] == "application/json":
                    js = await resp.json()
                    return js

                else:
                    raise errors.ApiError(f"{resp.status}. \
                    Request was great but Dagpi did not send a JSON")
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

        if not self.token:
            raise errors.Unauthorised("Please Provide a dagpi token")

        headers = {
            "Authorization": self.token,
            'User-Agent': self.user_agent
        }

        request_url = self.base_url + "/image" + url
        async with self.client.get(request_url, headers=headers,
                                   params=params) as resp:
            if 300 >= resp.status >= 200:
                if resp.headers["Content-Type"].lower() in \
                        ["image/png", "image/gif"]:
                    form = resp.headers["Content-Type"].replace("image/",
                                                                "")
                    resp_time = resp.headers["X-Process-Time"][:5]
                    raw_byte = await resp.read()
                    if self.logging:
                        log.info(
                            '[Dagpi Image] GET {} has returned {}'.format(
                                resp.url,
                                resp.status))
                    return Image(raw_byte, form, resp_time,
                                 params.get("url"))

                else:
                    raise errors.ApiError(f"{resp.status}. \
                Request was great but Dagpi did not send an Image back")
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
                    elif resp.status == 422:
                        try:
                            mstr = ""
                            for val in js["detail"]:
                                base = "{} is {}".format(val["loc"][1],
                                                         val["type"])
                                mstr += (base + "\t")
                            raise errors.ParameterError(mstr)
                        except KeyError:
                            raise errors.ApiError(
                                "API was unable to manipulate the Image")
                    else:
                        raise errors.ApiError("Unknown API Error Occurred")

    async def close(self):
        await self.client.close()
