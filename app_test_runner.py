#!/usr/bin/env python

import os
import sys

from optparse import OptionParser

from django.conf import settings
from django.core.management import call_command

def main():
    """
    The entry point for the script. This script is fairly basic. Here is a
 quick example of how to use it::
    
        app_test_runner.py [path-to-app]

    You must have Django on the PYTHONPATH prior to running this script. This
