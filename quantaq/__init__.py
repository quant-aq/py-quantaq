# -*- coding: utf-8 -*-
from getversion import get_module_version
import quantaq

__version__, _ = get_module_version(quantaq)

from .client import (
    ClientBase, 
    DevelopmentAPIClient, 
    StagingAPIClient, 
    ProductionAPIClient
    )

QuantAQAPIClient = ProductionAPIClient
