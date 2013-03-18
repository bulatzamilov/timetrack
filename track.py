#!/usr/bin/env python
# -*- coding: utf-8 -*-
# track.py

"""This script does logging of your activity. Each time you run it with yor activity as argument
it adds time in seconds passed since UNIX Epoch started"""

__author__    = 'Bulat Zamilov <bulat.zamilov@gmail.com>'
__version__   = '0.0.1'
__date__      = '2013 March 18'
__copyright__ = 'Copyright (c) 2013 Bulat Zamilov' 
__license__   = 'GPLv2'

from sys import argv
from time import time
from math import floor

def help():
    """Prints how to use track.py script"""
    print """
    Usage: ./timetrack TASK_NAME
    """ 

def main():
    """Reads arguments and puts time stamps into timelog.log"""
    if len(argv) == 1 or len(argv) > 2:
        help()
    else:
        delimiter = '#'
        log = open('timelog.log', 'a+') # mode - append with multiple option of reading
        # log.seek(0,2)
        log.write(str(int(floor(time()))) + '\n')
        log.write(argv[1] + delimiter + str(int(floor(time()))) + delimiter)
        log.close()

if __name__ == '__main__':
    main()
