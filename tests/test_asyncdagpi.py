from datetime import datetime
import os

import pytest

from asyncdagpi import Client, errors, ImageFeatures, Image, Ratelimits

def test_url_regex():
    for url in ["hpps://dagbot.com", "http//dagbot.com", "https://dagcom"]:
        try:
            Client.url_test(url)
        except Exception as e:
            print(str(e))
            assert isinstance(e, errors.BadUrl)


@pytest.mark.asyncio
async def test_no_auth():
    c = Client("bad token")
    try:
        await c.wtp()
    except Exception as e:
        assert isinstance(e, errors.Unauthorised)
    await c.close()


@pytest.mark.asyncio
async def test_feature_check():
    tok = os.getenv("DAGPI_TOKEN")
    c = Client(tok)
    try:
        await c.image_process('bad', 'https://dagbot-is.the-be.st/logo.png')
    except Exception as e:
        assert isinstance(e, errors.InvalidFeature)
    await c.close()


@pytest.mark.asyncio
async def test_feature_string_check():
    tok = os.getenv("DAGPI_TOKEN")
    c = Client(tok)
    img = await c.image_process(ImageFeatures.from_string('gay'), 'https://dagbot-is.the-be.st/logo.png')
    await c.close()
    assert isinstance(img, Image)

@pytest.mark.asyncio
async def test_image():
    tok = os.getenv("DAGPI_TOKEN")
    c = Client(tok)
    img = await c.image_process(ImageFeatures.pixel(),
                                "https://dagbot-is.the-be.st/logo.png")
    await c.close()
    img.write("some.png")
    assert isinstance(img, Image)
    assert isinstance(img.read(), bytes)
    assert isinstance(repr(img), str)
    assert isinstance(img.size(), int)


@pytest.mark.asyncio
async def test_image_special():
    tok = os.getenv("DAGPI_TOKEN")
    c = Client(tok)
    img = await c.special_image_process("https://dagbot-is.the-be.st/logo.png")
    await c.close()
    img.write("some.png")
    assert isinstance(img, Image)
    assert isinstance(img.read(), bytes)
    assert isinstance(repr(img), str)
    assert isinstance(img.size(), int)

@pytest.mark.asyncio
async def test_image_unaccesible():
    tok = os.getenv("DAGPI_TOKEN")
    c = Client(tok)
    try:
        await c.image_process(ImageFeatures.wanted(), "https://google.com")
    except Exception as e:
        assert isinstance(e, errors.ImageUnaccesible)
    await c.close()


@pytest.mark.asyncio
async def test_parameter_error():
    tok = os.getenv("DAGPI_TOKEN")
    c = Client(tok)
    try:
        await c.image_process(ImageFeatures.discord(),
                              "https://dagpi.xyz/dagpi.png")
    except Exception as e:
        assert isinstance(e, errors.ParameterError)
    await c.close()


@pytest.mark.asyncio
async def test_data():
    tok = os.getenv("DAGPI_TOKEN")
    c = Client(tok)
    dat = await c.wtp()
    assert dat.name
    pickup = await c.pickup_line()
    assert pickup.line
    headline = await c.headline()
    assert headline.headline
    logo = await c.logo()
    assert isinstance(str(logo), str)
    roast = await c.roast()
    assert isinstance(roast, str)
    yomama = await c.roast()
    assert isinstance(yomama, str)
    await c.close()

@pytest.mark.asyncio
async def test_data_objects():
    tok = os.getenv("DAGPI_TOKEN")
    c = Client(tok)
    cap = await c.captcha()
    assert cap.answer
    typ = await c.typeracer()
    assert typ.image
    await c.close()

@pytest.mark.asyncio
async def test_image_kwargs():
    tok = os.getenv("DAGPI_TOKEN")
    c = Client(tok)
    discord = await c.image_process(ImageFeatures.discord(), "https://dagbot-is.the-be.st/logo.png", text="Message", username="lol", dark=False)
    await c.close()
    assert isinstance(discord, Image)



@pytest.mark.asyncio
async def test_ping():
    tok = os.getenv("DAGPI_TOKEN")
    c = Client(tok)
    image_ping = await c.image_ping()
    assert image_ping > 0
    data_ping = await c.data_ping()
    assert data_ping > 0
    await c.close()
    assert isinstance(image_ping, float)

@pytest.mark.asyncio
async def test_rls():
    tok = os.getenv("DAGPI_TOKEN")
    c = Client(tok)
    image_ping = await c.joke()
    assert isinstance(c.ratelimits, Ratelimits)
    assert isinstance(c.ratelimits.limit, int)
    assert isinstance(repr(c.ratelimits), str)
    assert isinstance(c.ratelimits.remaining, int)
    assert isinstance(c.ratelimits.reset, datetime)

