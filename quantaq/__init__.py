# -*- coding: utf-8 -*-

__version__ = "0.1.0"
__author__ = "David H Hagan"
__author_email__ = "david.hagan@quant-aq.com"

from .baseapi import TokenError, NotFoundError, NotPermittedError, \
    BadRequestError

from .legacy import *