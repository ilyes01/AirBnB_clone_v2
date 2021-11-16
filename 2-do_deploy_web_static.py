#!/usr/bin/python3
"""
    Fabric script to automate deployment
"""
from fabric.api import run, put, local, env
from datetime import datetime
import os.path


env.hosts = ['34.73.100.0', '34.228.167.237']


def do_pack():
    """
     generates a .tgz archive from the contents of the web_static folder of
     your AirBnB Clone repo.
    """
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    path = 'versions/web_static_' + date + '.tgz'
    if not (os.path.exists("versions")):
        local('mkdir -p versions')
    local('tar -cvzf ' + path + ' web_static')
    if (os.path.exists(path)):
        return path
    return None


def do_deploy(archive_path):
    """fix that shit."""
    if not (os.path.exists(archive_path)):
            return False
    archive_name = archive_path.split('/')[1]
    archive_name_without_ext = archive_path.split('/')[1].split('.')[0]
    release_path = '/data/web_static/releases/' + archive_name_without_ext
    upload_path = '/tmp/' + archive_name
    put(archive_path, upload_path)
    run('mkdir -p ' + release_path)
    run('tar -xzf ' + upload_path + ' -C ' + release_path)
    run('rm ' + upload_path)
    run('mv ' + release_path + '/web_static/* ' + release_path + '/')
    run('rm -rf ' + release_path + '/web_static')
    run('rm -rf /data/web_static/current')
    run('ln -s ' + release_path + ' /data/web_static/current')
    return True
