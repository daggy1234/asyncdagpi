from asyncdagpi.http import http


class InvalidOption(Exception):
    pass


class Client:
    __slots__ = ("httpclient", "baseurl", "token")

    def __init__(self, authtoken: str):
        self.token = authtoken
        self.httpclient = http()
        self.baseurl = "http://dagpi.tk/api"

    def urlconstructor(self, func) -> str:
        return f"{self.baseurl}/{func}"

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

    async def staticimage(self, feature: str, image_url: str):
        feature_list = ["wanted", "evil", "bad", "hitler", "angel", "trash", "satan"]
        if feature not in feature_list:
            raise InvalidOption(f"{feature} is not a valid static feature")
        else:
            url = self.urlconstructor(feature)
            header = self.headerconstructor(image_url)
            response = await self.httpclient.post(url, header)
            return response

    async def gif(self, feature: str, image_url: str):
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
        ]
        if feature not in feature_list:
            raise InvalidOption(f"{feature} is not a valid gif feature")
        else:
            url = self.urlconstructor(feature)
            header = self.headerconstructor(image_url)
            response = await self.httpclient.post(url, header)
            return response

    async def usertextimage(
        self, feature: str, image_url: str, text: str, name: str = None
    ):
        feature_list = ["tweet", "quote"]
        if feature not in feature_list:
            raise InvalidOption(f"{feature} is not a valid usertextimage feature")
        else:
            url = self.urlconstructor(feature)
            header = self.headerconstructor(image_url, text, name)
            response = await self.httpclient.post(url, header)
            return response

    async def textimage(self, feature: str, image_url: str, text: str):
        feature_list = ["meme", "thoughtimage"]
        if feature not in feature_list:
            raise InvalidOption(f"{feature} is not a valid textimage feature")
        else:
            url = self.urlconstructor(feature)
            header = self.headerconstructor(image_url, text)
            response = await self.httpclient.post(url, header)
            return response

    async def close(self):
        await self.httpclient.close_session()
