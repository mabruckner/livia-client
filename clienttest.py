#!/usr/bin/env python3

"""
Usage:
    clienttest.py <url> <project> <apikey>
"""

import livia as client
import sys
import time
import math
print("connecting to "+sys.argv[1])
logger = client.logger(sys.argv[1], sys.argv[2], sys.argv[3])
print("Response: ")
print(logger.log("42"))
