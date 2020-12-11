QuickStart
==========

.. tip::
    These are just quick quide to get you started. Read the API reference to properly use the library.

Installation
------------

.. code:: shell

    pip install asyncdagpi

Data API
--------

Some endpoints like WTP, PickupLine and Logo will return Objects while
Waifu will return a Dictionary. Everything else will return a string.

.. code:: python

    from asyncdagpi import Client
    dagpi = Client("dagpi token")
    # For WTP Object
    wtp = await dagpi.wtp()
    # For Roast
    roast = await dagpi.roast()

Image Manipulation
------------------

All Image endpoints return an Image object. This has many properties
that can be useful for developers. Three basic implementations are displayed.

Discord.py
~~~~~~~~~~

.. code:: python

    from discord.ext import commands
    import discord
    from asyncdagpi import Client, ImageFeatures

    bot = commands.Bot(command_prefix="!")
    dagpi = Client("dagpi token")

    @bot.command()
    async def pixel(ctx, member: discord.Member):
        url = str(member.avatar_url_as(format="gif", static_format="png", size=1024))
        img = await dagpi.image_process(ImageFeatures.pixel(), url)
        file = discord.File(fp=img.image,filename=f"pixel.{img.format}")

Writing To File
~~~~~~~~~~~~~~~

.. code:: python

    from asyncdagpi import Client, ImageFeatures
    dagpi = Client("dagpi token")
    img = await dagpi.image_process(ImageFeatures.pixel(), "https://dagbot-is.the-be.st/logo.png")
    #it will auto chose the right format and write to current directory
    img.write("pixel")
    #will create pixel.png in this case

Python Pillow
~~~~~~~~~~~~~

.. code:: python

    from asyncdagpi import ImageFeatures, Client
    from PIL import Image

    dagpi = Client("dagpi token")
    img = await dagpi.image_process(ImageFeatures.pixel(), "https://dagbot-is.the-be.st/logo.png")
    im = Image.open(img.image)



