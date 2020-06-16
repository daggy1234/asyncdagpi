import asyncio
from asyncdagpi.client import client

async def main():

    apiclient = client('sgKb8C3zEI4J3o82hAQMn7ZYljGURV7u2UO5poLSwZknOBcIaX2vwbshw3JUbC2K')
    wanted = await apiclient.staticimage('wanted','https://dagbot-is.the-be.st/logo.png')
    await wanted.save('wanted.png')
    await client.close()

asyncio.get_event_loop().run_until_complete(main())
