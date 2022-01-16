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

    ftp = 1 if number == 0 else number
    remote_dir = '/data/web_static/releases/'

    list_dir = os.listdir('versions')
    list_dir.sort()
    num_archives = len(list_dir)
    iteration = num_archives - ftp

    if iteration < 0:
        return

    for dir_index in range(iteration):
        local('rm -r ./versions/{}'.format(list_dir[dir_index]))
    
    r_dir_list = run('ls -tr {}'.format(remote_dir))
    for ri in range(iteration):
        run('rm -r {}{}'.format(r_dir_list[ri]))
