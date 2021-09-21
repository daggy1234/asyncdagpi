from io import BytesIO
from typing import Optional


class Image(object):

    """
    An AsyncDagpi Image Returned
    This has special properties that can enhance the experience.

    .. container:: Attributes

        **Attributes**

        image: :class:`io.BytesIO`
            BytesIO object with Image
        format: :class:`str`
            String containing Image Format
            Either PNG or GIF
        process_time: :class:`str`
            String for Time Taken by API to process Request
        original_image: :class:`str`
            URL for the image passed to the API
    """

    def __init__(self, byt: bytes, image_format: str, process_time: str,
                 original_url: str):
        """
        Initialise an asyncdagpi.Image
        """
        self.image: BytesIO = BytesIO(byt)
        self.format: str = image_format
        self.process_time: str = process_time
        self.original_image: str = original_url

    def size(self) -> int:
        """
        Returns the Size of the Image
        """
        return self.image.__sizeof__()

    def __repr__(self) -> str:
        """
        A description of the Image
        """
        return f"<asyncdagpi.Image format={self.format}>"

    def read(self) -> bytes:
        """
        Get raw Image bytes
        :return: :class:`bytes`
        """
        return self.image.read()

    def write(self, name: str, *, path: Optional[str] = None) -> None:
        """
        Writes the Image Object to file

        :param name: :class:`str`
            the name of the file to save
        kwargs: Optional To Pass in
            - path: path to write to can be relative/absolute. default is ./
        """
        path = path or "."
        with open("{}/{}.{}".format(path, name, self.format), 'wb') as file:
            file.write(self.read())
