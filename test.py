import asyncio
from asyncdagpi.client import client

async def main():

    apiclient = client('insertyourtoken')
    wanted = await apiclient.staticimage('wanted','https://dagbot-is.the-be.st/logo.png')
    await wanted.save('wanted.png')
    await client.close()

asyncio.get_event_loop().run_until_complete(main())
