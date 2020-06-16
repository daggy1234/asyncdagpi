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
