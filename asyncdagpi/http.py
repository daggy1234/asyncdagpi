"""
Copyright © 2020 Daggy1234

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""


import aiohttp
from io import BytesIO
from . import exceptions

class http:
    __slots__ = ("session", "codedict")

    def __init__(self):
        self.session = None
        self.codedict = {
            400: exceptions.BadUrl('The url passed is poorly framed'),
            404: exceptions.APIError(404,'Dagpi is down'),
            401: exceptions.IncorrectToken('Your token is invalid'),
            408: exceptions.ImageUnaccesible(408,"The API was unable to connect and download your image"),
            415: exceptions.ImageUnaccesible(415,"The API was unable to find an image at your url"),
            429: exceptions.RateLimited('You are being rate limited by the api.'),
            500: exceptions.APIError(500,'Internal API error'),
            413: exceptions.FileTooLarge("The image is too large to use")
        }

    async def session_create(self):
        self.session = aiohttp.ClientSession()
    async def getbytes(self,url):
        if self.session == None:
            await self.session_create()
        async with self.session.get(url) as r:
            byt = await r.read()
            io = BytesIO(byt)
            io.seek(0)
            return io
    async def post(self, url, headers):
        if self.session == None:
            await self.session_create()

        async with self.session.post(url, headers=headers) as r:
            if r.status == 200:
                json = await r.json()
                return (json['url'])
            else:
                try:
                    ectx = self.codedict[r.status]
                    raise ectx
                except KeyError:
                    ectx = exceptions.UnknownError(r.status)
                raise ectx

    async def close_session(self):
        if self.session != None:
            await self.session.close()
            self.session = None
