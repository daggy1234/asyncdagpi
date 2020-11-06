.. currentmodule:: asyncdagpi
=============
API reference
=============


Version Related Info
====================

\.\.\. There are two main ways to query version information about the library.

.. data:: version_info

    A named tuple that is similar to `sys.version_info`_.

    Just like `sys.version_info`_ the valid values for ``releaselevel`` are
    'alpha', 'beta', 'candidate' and 'final'.

    .. _sys.version_info: https://docs.python.org/3.6/library/sys.html#sys.version_info

.. data:: __version__

    A string representation of the version. e.g. ``'0.1.0-alpha0'``.

Client
======
This is the base asyncdagpi client you have to use to make request.

This example initalises a basic client

.. code:: python

  from asyncdagpi import Client
  client = Client("your token")

.. tip::
    You can also disable logging

.. code:: python

    from asyncdagpi import Client
    client = Client(token, logging=False)


You can also setup a more advance client by passing in your own aiohttp ClientSession and Event Loop.
in thd case of discord.py it is adviseable to use the *bot.loop* as the event loop.

.. warning::
  Please use this only if you know what you are doing

.. code:: python

  from asyncndagpi import Client
  loop = #Your Asyncio Event Loop
  session = #Your Aiohttp session
  client = Client(token, loop=loop, session=session)


Given Below is All of the methods of the Client.

Client
------

.. autoclass:: Client
    :members:
.. danger::
  Closing the CLient means a new one must be initialised otherwise there will be errors.
ImageFeatures
=============

.. autoclass:: ImageFeatures
    :members:

Response Models
===============

Image Response
--------------

.. autoclass:: Image
    :members:

Data Response Models
--------------------

Data Objects returbed by some Data API endpoints. The base class is.

.. autoclass:: BaseDagpiObject
    :members:

All the below models are subclasses and will have all the same methods available to them.

WTP
~~~

.. autoclass:: WTP
    :members:

Logo
~~~~

.. autoclass:: Logo
    :members:

PickupLine
~~~~~~~~~~

.. autoclass:: PickupLine
    :members:

Errors
======

Asyncdagpi has Custom Exception the

.. tip:: AsyncDagpiExcpetion

  This is the base excpetion

AsyncDagpiExcpetion
-------------------

The base asyncdagpi excpetions

Use this to catch errors from the wrapper


SubExcpetions
~~~~~~~~~~~~~

.. py:exception:: errors.BadUrl

    The url provided is poorly framed

.. py:exception:: errors.Unauthorised

    Raised for an API 401

.. py:exception:: errors.RateLimited

    You are exceeding the API's rate limits and built in Ratelimit handler
    Essentially a 429

.. py:exception:: errors.FileTooLarge

    The image at source exceeds 10 MegaBytes

.. py:exception:: errors.InvalidFeature

    The feature chosen is not valid Chose a valid feature from asyncdagpi.ImageFeature

.. py:exception:: errors.ParameterError

    Parameters passed were not Sufficient

.. py:exception:: errors.ApiError

    The equivalent of a 500, for the API when the status code returned indicates an API issue.

.. py:exception:: errors.ImageUnaccesible

    The API was unable to get an image at your location

    .. container:: Attributes

        error_code: :class:`int`
            Containes the Code that the API returned
        message: :class:`str`
            returns info about the reason image was unaccesible


    .. py:function:: __str__

        Returns a Concatenated HTTP code and Message





