# asyncdagpi
An async wrapper for http://dagpi.tk

[![Build Status](https://travis-ci.com/Daggy1234/asyncdagpi.svg?branch=master)](https://travis-ci.com/Daggy1234/asyncdagpi)[![License](https://img.shields.io/github/license/daggy1234/asyncdagpi)](https://mit-license.org/)[![codestyle](https://img.shields.io/badge/code%20style-black-000000.svg)](https://pypi.org/project/black/) [version](https://img.shields.io/pypi/v/asyncdagpi) [python](https://img.shields.io/pypi/pyversions/asyncdagpi) 

## Documentation for asyncdagpi

### 1) Obtain a token

- - -
Join the discord server [here](http://server.daggy.tech) and verify yourself. Once done you can easily apply for a token via the process detailed.

### 2) Install the library

- - -

Use pip to install the library

```shell script
pip install asyncdagpi
```

### 3) Initialise the client

- - -

```python
from asycncdagpi import Client
API_CLIENT = Client('insert_your_token')
```

With this you should have a working API client that can help you authenticate and process api requests

### 4) Use One of the Features listed below with your client instance

- - -

- staticimage
- gif
- usertextimage
- textimage

These categories have a lot of features. A list of features can be found below or in the API documentation at 
[docs](http://dagpi.tk/docs)

You can use the client with a feature as follows:

```python
async def wanted(image_url:str):
    response = await API_CLIENT.staticimage('wanted'image_url)
```

### 5) Using the Response

- - -

The client returns an BytesIO object as a default response. The BytesIO response can be used in a lot of ways. Read the documentation here : [BytesIOdocs](https://docs.python.org/3/library/io.html) in the BytesIO section.

The examples below depict a few use cases

**Saving Response to file**

```python
async def wanted(image_url:str):
    response = await API_CLIENT.staticimage('wanted',image_url)
    with open('wanted.png''wb') as out:
        out.write(response.read())
```

**Opening The response with Pillow (PIL)**

```python
from PIL import Image
async def wanted(image_url:str):
    response = await API_CLIENT.staticimage('wanted',image_url)
    image = Image.open(response)
```

**Using the Discord.py library and sending response as a file**

`please do remember to get a discord api token and run the bot using that.`

Get help with discord.py at [dpy server](https://discord.gg/dpy)

```python

import discord
from discord.ext import commands
bot = commands.Bot(command_prefix = '.')
@bot.command()
async def wanted(ctximage_url:str):
    response = await API_CLIENT.staticimage('wanted',image_url)
    file = discord.File(response,filename='wanted.png')
    await ctx.send(file=file)  
```

### 6) Handling Exceptions

- - -

#### -  InvalidOption

This exception is raised when the feature chose ie. wanted is not a valid feature from the available options.

#### -  BadUrl

The api uses regex to validate urls. When an improper url is passed to the API this exception is raised

#### -  ValueError

This is when the API returns a non 200 code ie means an error occurred. This exception throws the status code along with a message explaining the status code. The description of status codes can be found in the API docs.

### Categories and their subsequent features

- - -

### staticimage

This returns an png image (as BytesIO) and requires the image_url for a static image.

 ```python
API_CLIENT.usertextimage(feature,image_url)

# feature - one of the features
# image_url - a static image url
```

Features:

- wanted
- evil
- bad
- hitler
- angel
- trash
- satan

### Gif

Returns a gif (as BytesIO). Takes either  a static_image url or a gif url and returns a gif. Irrespective of the inupt output is always a gif.

 ```python
API_CLIENT.usertextimage(feature,image_url)

# feature - one of the features
# image_url - a gif or static image_url
```

Features:

- paint
- solar
- blur
- invert
- pixel
- sepia
- wasted
- gay
- charcoal

### usertextimage

Returns a png (as BytesIO). Takes in the following arguments

```python
API_CLIENT.usertextimage(feature,image_url,text,name)

# feature - one of the features
# image_url - a static image url
# text - the text the person will say
# name - the username that will be used for the person
```

Features:

- tweet
- quote (discord message)

#### textimage

Depending in the feature and imput either returns a static or gif image as BytesIO.

```python
API_CLIENT.usertextimage(feature,image_url,text)

# feature - one of the features
# image_url - a static image url
# text - the text the person will say
```

Features:

- Thoughtimage: always returns a static response
- meme : based in type of input image_url returns a gif or png as BytesIO
