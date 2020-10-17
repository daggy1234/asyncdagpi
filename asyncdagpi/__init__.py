# -*- coding: utf-8 -*-

"""
Asyncdagpi
~~~~~~~~~~~~~~~~~~~
An async wrapper for dagpi
:copyright: (c) 2020 Daggy
:license: MIT, see LICENSE for more details.
"""

from collections import namedtuple

__title__ = "asyncdagpi"
__author__ = "Daggy1234"
__license__ = "MIT"
__copyright__ = "Copyright 2020 Daggy1234"
__version__ = "3.0.0"

from .http import HTTP
from .image_features import ImageFeatures
from .client import Client
from .image import Image
from .objects import WTP, Logo, PickupLine

VersionInfo = namedtuple("VersionInfo", "major minor micro releaselevel serial")

version_info = VersionInfo(major=2, minor=0, micro=0, releaselevel="stable", serial=0)
