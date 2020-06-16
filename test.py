import asyncio
from asyncdagpi.client import Client


async def main():

    apiclient = Client("token")
    wanted = await apiclient.staticimage(
        "wanted", "https://dagbot-is.the-be.st/logo.png"
    )
    byt = wanted.read()
    with open("wanted.png", "wb") as out:
        out.write(byt)
    await apiclient.close()


asyncio.get_event_loop().run_until_complete(main())
