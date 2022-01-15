#!/usr/bin/python3
"""
Fabric script based on the file 2-do_deploy_web_static.py that creates and
distributes an archive to the web servers
"""

from fabric.api import *
from datetime import datetime
import os
env.hosts = ['142.44.167.228', '144.217.246.195']


def do_pack():
    """
    This packs files in ./web_static/ into a tar.tgz file
    in ./versions/
    """
    time_data = datetime.utcnow()
    ft = '{}{}{}{}{}{}'.format(
        time_data.year,
        time_data.month,
        time_data.day,
        time_data.hour,
        time_data.minute,
        time_data.second
    )
    if not os.path.exists('./versions'):
        os.mkdir('./versions')
    formatedpath = './versions/web_static_{}.tgz web_static'.format(ft)
    print(formatedpath)
    local('tar -cvzf {}'.format(formatedpath))
    return formatedpath


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
            run('tar -xvf /tmp/{} -C {}'.format(archive_name, targetfolder))
            run('mv {}web_static {}{}'.format(
                targetfolder, targetfolder, archive_no_ext))
            run('rm /tmp/{}'.format(archive_name))
            run('rm -rf {}'.format(sym_path))
            run('ln -s {}{} {}'.format(targetfolder, archive_no_ext, sym_path))
            return True
    except BaseException as e:
        print(e)
        return False


def deploy():
    """This deploys files to the webserver by compiling
    ./web_static into an archive .tgz file and deploying it to the
    webserver
    """
    a_path = do_pack()
    if a_path is None:
        return False
    return do_deploy(a_path)
