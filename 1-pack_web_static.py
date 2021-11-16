#!/usr/bin/python3
"""
Fabric script that generates a .
"""
from fabric.api import run, put, local
from datetime import datetime
import os.path


def do_pack():
"""
generates
"""

    date = datetime.now().strftime("%Y%m%d%H%M%S")
    path = 'versions/web_static_' + date + '.tgz'
    if not (os.path.exists("versions")):
        local('mkdir -p versions')
    local('tar -cvzf ' + path + ' web_static')
    if (os.path.exists(path)):
        return path
    return None
