#!/usr/bin/python3

"""
This module packs the files on webstatic into
a tar archive file
"""

from datetime import datetime
import os
from fabric.api import *


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
