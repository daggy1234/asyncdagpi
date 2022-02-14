.. currentmodule:: asyncdagpi.errors
======
Errors
======

Asyncdagpi incorporates custom exceptions

.. tip:: AsyncDagpiException

  This is the base excpetion

AsyncDagpiException
-------------------

The base asyncdagpi exceptions

Use this to catch errors from the wrapper


SubExceptions
-------------

.. py:exception:: BadUrl

    The url provided is poorly framed

.. py:exception:: Unauthorised

    Raised for an API 401

.. py:exception:: RateLimited

    You are exceeding the API's rate limits and built in Ratelimit handler
    Essentially a 429

.. py:exception:: FileTooLarge

    The image at source exceeds 10 MegaBytes

.. py:exception:: InvalidFeature

    The feature chosen is not valid Chose a valid feature from asyncdagpi.ImageFeature

.. py:exception:: ParameterError

    Parameters passed were not Sufficient

.. py:exception:: ApiError

    The equivalent of a 500, for the API when the status code returned indicates an API issue.

.. py:exception:: ImageUnaccesible

    The API was unable to get an image at your location

    .. container:: Attributes

        error_code: :class:`int`
            Containes the Code that the API returned
        message: :class:`str`
            returns info about the reason image was unaccesible


    .. py:function:: __str__

        Returns a Concatenated HTTP code and Message





