# -*- coding: utf-8 -*-

"""

Asyncdagpi
~~~~~~~~~~~~~~~~~~~
An async wrapper for dagpi
:copyright: (c) 2020 Daggy
:license: MIT, see LICENSE for more details.
"""

import logging
from typing import NamedTuple
from .image_features import ImageFeatures
from .client import Client
from .image import Image
from .objects import WTP, Logo, PickupLine, BaseDagpiObject, Ratelimits

__title__: str = "asyncdagpi"
__author__: str = "Daggy1234"
__license__: str = "MIT"
__copyright__: str = "Copyright 2021 Daggy1234"
__version__: str = '4.0.0'


class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: str
    serial: int


version_info: VersionInfo = VersionInfo(major=4, minor=0, micro=0, releaselevel='alpha',
                                        serial=0)

logging.getLogger(__name__).addHandler(logging.NullHandler())
