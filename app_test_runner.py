#!/usr/bin/env python

import os
import sys

from optparse import OptionParser

from django.conf import settings
from django.core.management import call_command

def main():
    """
  The entry point for the script. This script is fairly basic. Here is a
