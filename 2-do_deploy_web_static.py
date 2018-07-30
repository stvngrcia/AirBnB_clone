#!/usr/bin/python3
"""This have do_deploy function"""
import os
from fabric.api import *

env.user = "ubuntu"
env.hosts = ['35.237.55.203', '104.196.13.174']


def do_deploy(archive_path):
    """distributes an archive to your web servers, using the function"""
    if (os.path.isfile(archive_path) is False):
        return False
    path = archive_path.split('/')[1]
    target = "/data/web_static/releases/" + path
    try:
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}/".format(target))
        run("sudo tar -xzf /tmp/{} -C {}/".format(path, target))
        run("sudo rm /tmp/{}".format(path))
        run("sudo mv {}/web_static/* {}/".format(target, target))
        run("sudo rm -rf {}/web_static".format(target))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(target))
        print("New version deployed")
        return True
    except Exception:
        return False
