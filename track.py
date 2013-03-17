#!/usr/bin/env python
# -*- coding: utf-8 -*-
# track.py

__author__    = 'cyberbolt <cyberbolt@rambler.ru>'
__version__   = '$Revision: 0.0.1 $'
__date__      = '$Date: 2013 March 17$'
__copyright__ = 'Bulat Zamilov'
__license__   = 'GPLv2'

from sys import argv
from time import time
from math import floor

def help():
    print """
    Usage: ./timetrack TASK_NAME
    """ 

if __name__ == '__main__':
    
    if len(argv) == 1 or len(argv) > 2:
        help()
    else:
        delimiter = '#'
        log = open('timelog.log', 'a+') # mode - append with multiple option of reading
        # log.seek(0,2)
        log.write(str(int(floor(time()))) + '\n')
        log.write(argv[1] + delimiter + str(int(floor(time()))) + delimiter)
        log.close()
