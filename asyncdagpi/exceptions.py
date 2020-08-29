from http import HTTPStatus
class InvalidOption(Exception):
    """Raised when you choose an option not in the featurelist"""
    pass

class BadUrl(Exception):
    """The url passed is poorly frames"""
    pass


class IncorrectToken(Exception):
    """API authorisation failure"""
    pass

class RateLimited(Exception):
    """You are exceeding the API's rate limits"""
    pass
class APIError(Exception):
    """API has undergone an error"""
    def __init__(self,error_code,message):
        self.errorcode = error_code
        self.message = message
    def __str__(self):
        return f'{self.errorcode} ---> {self.message}'

class FileTooLarge(Exception):
    """The image is too large for the API"""
    pass
class UnknownError(Exception):
    """HTTP Status code not known"""
    def __init__(self,code):
        self.httplist = list(HTTPStatus)
        self.code = code
    def geterrormessage(self):
        for code in self.httplist:
            if code.value == self.code:
                return (code.description)
        else:
            return "Unknown Error Code"
    def __str__(self):
        return f'{self.code} -> {self.geterrormessage()}'

class ImageUnaccesible(Exception):
    """The API was unable to retrive an image"""
    def __init__(self,error_code,message):
        self.errorcode = error_code
        self.message = message
    def __str__(self):
        return f'{self.errorcode} ---> {self.message}'


