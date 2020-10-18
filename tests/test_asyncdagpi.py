import os

import pytest

from asyncdagpi import Client, errors, ImageFeatures, Image


def test_url_regex():
    for url in ["hpps://dagbot.com", "http//dagbot.com", "https://dagcom"]:
        try:
            Client.url_test(url)
        except Exception as e:
            print(str(e))
            assert isinstance(e, errors.BadUrl)


@pytest.mark.asyncio
async def test_no_auth():
    c = Client("")
    try:
        await c.wtp()
    except Exception as e:
        assert isinstance(e, errors.Unauthorised)


@pytest.mark.asyncio
async def test_feature_check():
    tok = os.getenv("DAGPI_TOKEN")
    c = Client(tok)
    try:
        await c.image_process('bad', 'https://dagbot-is.the-be.st/logo.png')
    except Exception as e:
        assert isinstance(e, errors.InvalidFeature)


@pytest.mark.asyncio
async def test_image():
    tok = os.getenv("DAGPI_TOKEN")
    c = Client(tok)
    img = await c.image_process(ImageFeatures.pixel(),
                                "https://dagbot-is.the-be.st/logo.png")
    assert isinstance(img, Image)


@pytest.mark.asyncio
async def test_image_unaccesible():
    tok = os.getenv("DAGPI_TOKEN")
    c = Client(tok)
    try:
        omg = await c.image_process(ImageFeatures.wanted(), "https://google.com")
    except Exception as e:
        assert isinstance(e, errors.ImageUnaccesible)

@pytest.mark.asyncio
async def test_data():
    tok = os.getenv("DAGPI_TOKEN")
    c = Client(tok)
    dat = await c.wtp()
    assert dat.name
    logo = await c.logo()
    assert isinstance(str(logo), str)


@pytest.mark.asyncio
async def test_ping():
    tok = os.getenv("DAGPI_TOKEN")
    c = Client(tok)
    image_ping = await c.image_ping()
    assert isinstance(image_ping, float)

