# -*- coding: utf-8 -*-
from pkg_resources import get_distribution

from .baseapi import TokenError, NotFoundError, NotPermittedError, \
    BadRequestError

from .legacy import *

__version__ = get_distribution("opcsim").version