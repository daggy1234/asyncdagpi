"""
Copyright © 2020 Daggy1234

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""


import aiohttp
from io import BytesIO


class http:
    __slots__ = ("session", "codedict")

    def __init__(self):
        self.session = None
        self.codedict = {
            400: "Invalid link",
            404: "The api is down rightnow",
            401: "Invalid token",
            400: "Unable to use url",
        }

    async def session_create(self):
        self.session = aiohttp.ClientSession()

    async def returnresponse(self, option, response):
        if self.session == None:
            await self.session_create()
            if option:
                async with self.session.get(response) as r:
                    byt = await r.read()
                    io = BytesIO(byt)
                    io.seek(0)
                    return (io)
            else:
                return (response)

    async def post(self, url, headers):
        if self.session == None:
            await self.session_create()

        async with self.session.post(url, headers=headers) as r:
            if r.status == 200:
                bytes = await r.read()
                io = BytesIO(bytes)
                io.seek(0)
                return io
            else:
                try:
                    ectx = self.codedict[r.status]
                except KeyError:
                    ectx = "Unknown Exception"
                raise ValueError(f"Raised {r.status}:{ectx}")

    async def close_session(self):
        if self.session != None:
            await self.session.close()
            self.session = None
