import asyncio
from asyncdagpi.client import Client
import os

token = os.environ.get("token")
if not token:
    raise OSError("There is no token")


async def main(token):

    apiclient = Client(token)
    wanted = await apiclient.staticimage(
        "wanted", "https://dagbot-is.the-be.st/logo.png"
    )

    await apiclient.close()


asyncio.get_event_loop().run_until_complete(main(token))
