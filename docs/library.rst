.. currentmodule:: asyncdagpi
=============
API reference
=============


Version Related Info
--------------------

\.\.\. There are two main ways to query version information about the library.

.. data:: version_info

    A named tuple that is similar to `sys.version_info`_.

    Just like `sys.version_info`_ the valid values for ``releaselevel`` are
    'alpha', 'beta', 'candidate' and 'final'.

    .. _sys.version_info: https://docs.python.org/3.6/library/sys.html#sys.version_info

.. data:: __version__

    A string representation of the version. e.g. ``'0.1.0-alpha0'``.

Client
------
This is the base asyncdagpi client you use to make requests.

This example initalises a basic client.

.. code:: python

  from asyncdagpi import Client
  client = Client("your token")

.. tip::
    You can also disable logging

.. code:: python

    from asyncdagpi import Client
    client = Client(token, logging=False)


You can also setup a more advance client by passing in your own aiohttp ClientSession and Event Loop. 
If you are using discord.py it is adviseable to use the *bot.loop* as the event loop.

.. warning::
  Please use this only if you know what you are doing. Do not use the aiohttp session used by discord.py.

.. code:: python

  from asyncndagpi import Client
  loop = #Your Asyncio Event Loop
  session = #Your Aiohttp session
  client = Client(token, loop=loop, session=session)


Below is all of the methods of the client.

Client
~~~~~~

.. autoclass:: Client
    :members:
.. danger::
  Closing the Client means a new one must be initialised otherwise there will be errors.

