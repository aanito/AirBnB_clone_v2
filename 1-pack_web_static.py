#!/usr/bin/python3
"""a Fabric script that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo,
using the function do_pack"""
from datetime import datetime
from fabric.api import local


def do_pack():
    """Generate a .tgz file"""
    try:
        current_time = datetime.now()
        format_date = current_time.strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")
        path = "versions/web_static_{}.tgz".format(format_date)
        local("tar -cvzf {} web_static".format(path))
        return path
    except Exception as NotCreated:
        return None

