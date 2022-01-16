#!/usr/bin/python3

"""
This module cleans up outdated arhcives
"""

import os
from fabric.api import *


def do_clean(number=0):
    """
    This cleans old archives
        Args:
            number: This is the 
            number of archives to keep
    """

    iteration = 1 if number == 0 else number
    remote_dir = '/data/web_static/releases/'

    "clean locally"
    list_dir = os.listdir('versions')
    list_dir.sort()
    dir_len = len(list_dir)
    for dir_index in range(iteration):
        local('rm -r ./versions/{}'.format(list_dir[dir_index]))
    
    "clean remotely"
    r_dir_list = run('ls -tr {}'.format(remote_dir))
    for ri in range(number):
        run('rm -r {}{}'.format(r_dir_list[ri]))