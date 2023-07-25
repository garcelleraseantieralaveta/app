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
    script basically will bootstrap a Django environment for you.
    
    By default this script with use SQLite and an in-memory database. If you
    are using Python 2.5 it will just work out of the box for you.
    
    TODO: show more options here.
    """
    parser = OptionParser()
 parser.add_option("--DATABASE_ENGINE", dest="DATABASE_ENGINE", default="sqlite3")
  parser.add_option("--DATABASE_NAME", dest="DATABASE_NAME", default="")
 parser.add_option("--DATABASE_USER", dest="DATABASE_USER", default="")
