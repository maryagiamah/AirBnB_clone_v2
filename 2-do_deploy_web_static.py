#!/usr/bin/python3
"""distributes an archive to your web servers"""
from fabric.api import env, put, sudo
import os

env.hosts = ['54.175.134.91', '100.25.104.180']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """Deploys the archive to the web servers"""

    if not os.path.exists(archive_path):
        return False
    try:
        arch_name = archive_path.split('/')[-1]
        arch_wext = arch_name.split('.')[0]
        path = '/data/web_static/releases/'

        put(archive_path, "/tmp/")
        sudo(f"mkdir -p {path}{arch_wext}")
        sudo(f"tar -xzf /tmp/{arch_name} -C {path}{arch_wext}")
        sudo(f"rm /tmp/{arch_name}")
        sudo(f"mv {path}{arch_wext}/web_static/* {path}{arch_wext}")
        sudo(f"rm -rf {path}{arch_wext}/web_static")
        sudo("rm -rf /data/web_static/current")
        sudo(f"ln -s {path}{arch_wext} /data/web_static/current")
        return True
    except Exception as e:
        return False
