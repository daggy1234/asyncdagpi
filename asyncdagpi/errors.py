class AsyncDagpiException(Exception):
    """
    AsyncDagpi base exception class use this base class to catch any AsyncDagpi errors.
    """
    pass


class AsyncDagpiHttpException(AsyncDagpiException):
    """
    AsyncDagpi base exception class use this base class to catch any AsyncDagpi errors.
    """

    def __init__(self, status: int, message: str) -> None:
        self.status: int = status
        self.message: str = message
        super().__init__(message)


class ApiError(AsyncDagpiHttpException):
    """
    Raised when Dagpi has an error it does not know how to handle
    """

    def __init__(self, message: str) -> None:
        super().__init__(500, message)


class BadUrl(AsyncDagpiHttpException):
    """
    Exception raised when the URL is poorly framed or not of type String
    """

    def __init__(self, message: str) -> None:
        super().__init__(400, message)


class Unauthorised(AsyncDagpiHttpException):
    """
    Raised for an API 401
    """

    def __init__(self, message: str) -> None:
        super().__init__(401, message)


class RateLimited(AsyncDagpiHttpException):
    """
    You are exceeding the API's rate limits and built in Ratelimit handler
    Essentially a 429
    """

    def __init__(self, message: str) -> None:
        super().__init__(429, message)


class FileTooLarge(AsyncDagpiHttpException):
    """
    The image at source exceeds 10 MegaBytes
    """

    def __init__(self, message: str) -> None:
        super().__init__(413, message)


class InvalidFeature(AsyncDagpiException):
    """
    The feature chosen is not valid
    """
    pass


class ImageUnaccesible(AsyncDagpiHttpException):
    """
    The API was unable to get an image at your location
    """

    def __init__(self, error_code: int, message: str):
        """
        Initialise the ImageUnaccessible Error
        """
        self.error_code: int = error_code
        self.message: str = message
        super(ImageUnaccesible, self).__init__(self.error_code,
                                               f'{self.error_code} ---> \
        {self.message}')

    def __str__(self) -> str:
        """
        String Explaining the error
        :return: :class:`str`
        """
        return f'{self.error_code} ---> {self.message}'


class ParameterError(AsyncDagpiHttpException):
    """
    Parameters passed were not Sufficient
    """

    def __init__(self, message: str) -> None:
        super().__init__(400, message)
