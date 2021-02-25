# asyncdagpi

[![Build Status](https://travis-ci.com/Daggy1234/asyncdagpi.svg?branch=master)](https://travis-ci.com/Daggy1234/asyncdagpi) [![License](https://img.shields.io/github/license/daggy1234/asyncdagpi)](https://mit-license.org/) ![version](https://img.shields.io/pypi/v/asyncdagpi) [![python](https://img.shields.io/pypi/pyversions/asyncdagpi)](https://pypi.org/p/asyncdagpi) [![Documentation Status](https://readthedocs.org/projects/asyncdagpi/badge/?version=latest)](https://asyncdagpi.readthedocs.io/en/latest/?badge=latest) [![Codecov](https://img.shields.io/codecov/c/github/daggy1234/asyncdagpi?logo=codecov)](https://codecov.io/gh/daggy1234/asyncdagpi) [![Codacy Badge](https://app.codacy.com/project/badge/Grade/ad36f1ea6211444792e84f32a14326dd)](https://www.codacy.com/gh/Daggy1234/asyncdagpi/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Daggy1234/asyncdagpi&amp;utm_campaign=Badge_Grade)

Powerful Asynchronous Wrapper for dagpi [dagpi.xyz](https://dagpi.xyz)

## Installation

```shell script
pip install asyncdagpi
```

## Data API

Some endpoints like WTP, PickupLine and Logo will return Objects while Waifu will return a Dictionary. Everything else will return a string.

```python
from asyncdagpi import Client
dagpi = Client("dagpi token")
# For WTP Object
wtp = await dagpi.wtp()
#For Roast
roast = await dagpi.roast()
```

## Image Manipulation

All Image endpoints return an Image object. This has many properties that can be useful for developers. For Basic implementations are displayed

### Discord.py

```python
from discord.ext import commands
import discord
from asyncdagpi import Client, ImageFeatures

bot = commands.Bot(command_prefix="!")
dagpi = Client("dagpi token")

@bot.command()
async def pixel(ctx, member: discord.Member):
    url = str(member.avatar_url_as(static_format="png", size=1024))
    img = await dagpi.image_process(ImageFeatures.pixel(), url)
    file = discord.File(fp=img.image,filename=f"pixel.{img.format}")

```

### Writing To File

```python
from asyncdagpi import Client, ImageFeatures
dagpi = Client("dagpi token")
img = await dagpi.image_process(ImageFeatures.pixel(), "https://dagbot-is.the-be.st/logo.png")
#it will auto chose the right format and write to current directory
img.write("pixel")
#will create pixel.png in this case
```

### Python Pillow

```python
from asyncdagpi import ImageFeatures, Client
from PIL import Image

dagpi = Client("dagpi token")
img = await dagpi.image_process(ImageFeatures.pixel(), "https://dagbot-is.the-be.st/logo.png")
im = Image.open(img.image)
```

### Kwargs Example

```python
from asyncdagpi import ImageFeatures, Client

dagpi = Client("dagpi token")
img = await dagpi.image_process(ImageFeatures.tweet(), "https://dagbot-is.the-be.st/logo.png", text="This is asyncdagpi tweeting live from dagpi.xyz!", username="Asyncdagpi")
```

### For More Thorough Examples and Feature list read the documentation

[Docs](https://asyncdagpi.rtfd.io)
