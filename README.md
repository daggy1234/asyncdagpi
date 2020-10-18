# asyncdagpi

[![Build Status](https://travis-ci.com/Daggy1234/asyncdagpi.svg?branch=master)](https://travis-ci.com/Daggy1234/asyncdagpi) [![License](https://img.shields.io/github/license/daggy1234/asyncdagpi)](https://mit-license.org/) ![version](https://img.shields.io/pypi/v/asyncdagpi) ![python](https://img.shields.io/pypi/pyversions/asyncdagpi) [![Documentation Status](https://readthedocs.org/projects/asyncdagpi/badge/?version=latest)](https://asyncdagpi.readthedocs.io/en/latest/?badge=latest)[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FDaggy1234%2Fasyncdagpi.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2FDaggy1234%2Fasyncdagpi?ref=badge_shield)


Powerful Asynchronous Wrapper for dagpi https://dagpi.xyz

Installation
----

```shell script
pip install asyncdagpi
```

Data API
---

Some endpoints like WTP, PickupLine and Logo will return Objects while Waifu will return a Dictionary. Everything else will return a string.
```python
from asyncdagpi import Client
dagpi = Client("dagpi token")
# For WTP Object
wtp = await dagpi.wtp()
#For Roast
roast = await dagpi.roast()
```

Image Manipulation
---
All Image endpoints return an Image object. This has many properties that can be useful for developers. For Basic implementations are displayed

#### Discord.py

```python
from discord.ext import commands
import discord
from asyncdagpi import Client, ImageFeatures

bot = commands.Bot(command_prefix="!")
dagpi = Client("dagpi token")

@bot.command()
async def pixel(ctx, member: discord.Member):
    url = str(member.avatar_url_as(format="png", static_format="gif", size=1024))
    img = await dagpi.image_process(ImageFeatures.pixel(), url)
    file = discord.File(fp=img.image,filename=f"pixel.{img.format}")

```

#### Writing To File

```python
from asyncdagpi import Client, ImageFeatures
dagpi = Client("dagpi token")
img = await dagpi.image_process(ImageFeatures.pixel(), "https://dagbot-is.the-be.st/logo.png")
#it will auto chose the right format and write to current directory
img.write("pixel")
#will create pixel.png in this case
```
#### Python Pillow
```python
from asyncdagpi import ImageFeatures, Client
from PIL import Image

dagpi = Client("dagpi token")
img = await dagpi.image_process(ImageFeatures.pixel(), "https://dagbot-is.the-be.st/logo.png")
im = Image.open(img.image)
```


### For More Thorough Examples and Feature list read the documentation.



## License
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FDaggy1234%2Fasyncdagpi.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2FDaggy1234%2Fasyncdagpi?ref=badge_large)