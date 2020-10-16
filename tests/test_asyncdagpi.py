import os

import pytest

from asyncdagpi import __version__, Client, errors, ImageFeatures, Image


def test_version():
    assert __version__ == '2.0.2'


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
