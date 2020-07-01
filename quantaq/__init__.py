# -*- coding: utf-8 -*-
from importlib_metadata import version
import quantaq

__version__ = version("py-quantaq")

from .client import (
    ClientBase, 
    DevelopmentAPIClient, 
    StagingAPIClient, 
    ProductionAPIClient
    )

QuantAQAPIClient = ProductionAPIClient
