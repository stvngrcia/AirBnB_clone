#!/usr/bin/python3
"""generates a .tgz archive from the contents of the web_static folder"""
from datetime import datetime
from fabric.operations import local


def do_pack():
    """pack the file into tgz format"""
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".format(
            datetime.now().strftime("%Y%m%d%H%M%S")))
        return "versions/web_static_{}.tgz".format(
            datetime.now().strftime("%Y%m%d%H%M%S"))
    except Exception:
        return None
