#!/usr/bin/python3
"""distributes an archive to your web servers"""
from fabric.api import *
import os

def do_deploy(archive_path):
    """Deploys the archive to the web servers"""

    if os.path.exists(archive_path) is False:
        return False

    arch_name = archive_path.split('/')[-1]
    arch_wext = arch_name.split('.')[0]
    path = '/data/web_static/releases/'
    try:
        local("mv archive_path /tmp/")
        local(f"mkdir -p {path}{arch_wext}/")
        local(f"tar -xzf /tmp/{arch_name} -C {path}{arch_wext}/")
        local(f"rm /tmp/{arch_name}")
        local(f"mv {path}{arch_wext}/web_static/* {path}{arch_wext}/")
        local(f"rm -rf {path}{arch_wext}/web_static")
        local("rm -rf /data/web_static/current")
        local(f"ln -s {path}{arch_wext} /data/web_static/current")
    except Exception as e:
        return False
    return True
