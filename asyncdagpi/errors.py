class AsyncDagpiException(Exception):
    """
    AsyncDagpi base exception class
    use this base class to catch any AsyncDagpi errors.
    """
    pass


class ApiError(AsyncDagpiException):
    """
    Raised when Dagpi has an error it does not know how to handle
    """
    pass


class BadUrl(AsyncDagpiException):
    """
    Exception raised when the URL is poorly framed or not of type String
    """
    pass


class Unauthorised(AsyncDagpiException):
    """
    Raised for an API 401
    """
    pass


class RateLimited(AsyncDagpiException):
    """
    You are exceeding the API's rate limits and built in Ratelimit handler
    Essentially a 429
    """
    pass


class FileTooLarge(AsyncDagpiException):
    """
    The image at source exceeds 10 MegaBytes
    """
    pass


class InvalidFeature(AsyncDagpiException):
    """
    The feature chosen is not valid
    """
    pass


class ImageUnaccesible(AsyncDagpiException):
    """
    The API was unable to get an image at your location
    """

    def __init__(self, error_code, message):
        self.error_code = error_code
        self.message = message
        super(ImageUnaccesible, self).__init__(self.error_code,
                                               f'{self.error_code} ---> \
        {self.message}')

    def __str__(self):
        """
        String Explaining the error
        :return: :class:`str`
        """
        return f'{self.error_code} ---> {self.message}'


class ParameterError(AsyncDagpiException):
    """
    Parameters passed were not Sufficient
    """
    pass
