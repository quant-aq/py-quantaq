# -*- coding: utf-8 -*-
from pkg_resources import get_distribution
import quantaq

__version__ = get_distribution("py-quantaq").version

from .client import (
    ClientBase, 
    DevelopmentAPIClient, 
    StagingAPIClient, 
    ProductionAPIClient
    )

QuantAQAPIClient = ProductionAPIClient
