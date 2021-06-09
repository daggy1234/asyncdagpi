# -*- coding: utf-8 -*-

"""

Asyncdagpi
~~~~~~~~~~~~~~~~~~~
An async wrapper for dagpi
:copyright: (c) 2020 Daggy
:license: MIT, see LICENSE for more details.
"""

from asyncdagpi.objects import WTP, Logo, PickupLine, BaseDagpiObject
from asyncdagpi.image import Image
from asyncdagpi.client import Client
from asyncdagpi.image_features import ImageFeatures
from asyncdagpi.http import HTTP
from typing import NamedTuple

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
