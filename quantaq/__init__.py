# -*- coding: utf-8 -*-
from getversion import get_module_version
import quantaq

__version__, _ = get_module_version(quantaq)

from .baseapi import TokenError, NotFoundError, NotPermittedError, \
    BadRequestError

from .legacy import *

