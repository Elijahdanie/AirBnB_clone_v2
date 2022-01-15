#!/usr/bin/python3
"""
This module distributes an archive to webserver using
protoptye do_deploy
"""

from fabric.api import *
import os

env.hosts = ['34.139.231.147', '3.238.84.58']


def do_deploy(archive_path):
    """
    This distributes the archive to webservers
    """
    try:
        if not os.path.exists(archive_path):
            return False
        else:
            archive_name = archive_path.split('/')[-1]
            archive_no_ext = archive_name.split('.')[0]
            targetfolder = '/data/web_static/releases/'
            sym_path = '/data/web_static/current'
            run('sudo mkdir -p {}'.format(targetfolder))
            run('sudo chown -Rh ubuntu:ubuntu /data/')
            put(archive_path, '/tmp/{}'.format(archive_name))
            run('tar -xvf /tmp/{} -C {}'.format(
                archive_name, targetfolder))
            run('mv {}web_static {}{}'.format(
                targetfolder, targetfolder, archive_no_ext))
            run('rm /tmp/{}'.format(archive_name))
            run('rm -rf {}'.format(sym_path))
            run('ln -sf {}{} {}'.format(
                targetfolder, archive_no_ext, sym_path))
            return True
    except BaseException as e:
        print(e)
        return False
