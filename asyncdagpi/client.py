"""
Copyright © 2020 Daggy1234

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""


from asyncdagpi.http import http
import re
import aiohttp



class InvalidOption(Exception):
    pass


class BadUrl(Exception):
    pass


class Client:
    __slots__ = ("httpclient", "baseurl", "token")

    def __init__(self, authtoken: str):
        self.token = authtoken
        self.httpclient = http()
        self.baseurl = "http://dagpi.tk/api"

    def urlconstructor(self, func) -> str:
        return f"{self.baseurl}/{func}"


    def validateurl(self, url):
        regex = re.compile(
            r"^(?:http|ftp)s?://"  # http:// or https://
            r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"  # domain...
            r"localhost|"  # localhost...
            r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"  # ...or ip
            r"(?::\d+)?"  # optional port
            r"(?:/?|[/?]\S+)$",
            re.IGNORECASE,
        )
        y = re.match(regex, url)
        if not y:
            raise BadUrl("The url passed is badly framed")

    def headerconstructor(self, image_url, text: str = None, name: str = None) -> dict:
        if name != None and text != None:
            postdict = {
                "token": self.token,
                "url": image_url,
                "name": name,
                "text": text,
            }
        elif text != None:
            postdict = {"token": self.token, "url": image_url, "text": text}
        else:
            postdict = {"token": self.token, "url": image_url}
        return postdict

    async def staticimage(self, feature: str, image_url: str,bytes=False):
        feature_list = ["wanted", "evil", "bad", "hitler", "angel", "trash", "satan"]
        if feature not in feature_list:
            raise InvalidOption(f"{feature} is not a valid static feature")
        else:
            url = self.urlconstructor(feature)
            header = self.headerconstructor(image_url)
            response = await self.httpclient.post(url, header)
            finalresponse = await self.httpclient.returnresponse(bytes,response)
            return (finalresponse)

    async def gif(self, feature: str, image_url: str,bytes=False):
        feature_list = [
            "paint",
            "solar",
            "blur",
            "invert",
            "pixel",
            "sepia",
            "wasted",
            "gay",
            "charcoal",
            "deepfry"
        ]
        if feature not in feature_list:
            raise InvalidOption(f"{feature} is not a valid gif feature")
        else:
            self.validateurl(image_url)
            url = self.urlconstructor(feature)
            header = self.headerconstructor(image_url)
            response = await self.httpclient.post(url, header)
            finalresponse = await self.httpclient.returnresponse(bytes, response)
            return (finalresponse)

    async def usertextimage(
        self, feature: str, image_url: str, text: str, name: str = None,bytes=False
    ):
        feature_list = ["tweet", "quote"]
        if feature not in feature_list:
            raise InvalidOption(f"{feature} is not a valid usertextimage feature")
        else:
            self.validateurl(image_url)
            url = self.urlconstructor(feature)
            header = self.headerconstructor(image_url, text, name)
            response = await self.httpclient.post(url, header)
            finalresponse = await self.httpclient.returnresponse(bytes, response)
            return (finalresponse)

    async def textimage(self, feature: str, image_url: str, text: str,bytes=False):
        feature_list = ["meme", "thoughtimage"]
        if feature not in feature_list:
            raise InvalidOption(f"{feature} is not a valid textimage feature")
        else:
            self.validateurl(image_url)
            url = self.urlconstructor(feature)
            header = self.headerconstructor(image_url, text)
            response = await self.httpclient.post(url, header)
            finalresponse = await self.httpclient.returnresponse(bytes, response)
            return (finalresponse)
    async def close(self):
        await self.httpclient.close_session()
