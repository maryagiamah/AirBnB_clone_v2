#!/usr/bin/python3
"""distributes an archive to your web servers"""
from fabric.api import env, put, run
import os

env.hosts = ['54.175.134.91', '100.25.104.180']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """Deploys the archive to the web servers"""

    if not os.path.exists(archive_path):
        return False

    try:
        arch_name = archive_path.split('/')[-1]
        arch_wext = arch_name.split('.')[0]

        put(archive_path, f"/tmp/{arch_name}")
        run(f"mkdir -p /data/web_static/releases/{arch_wext}/")
        run(f"tar -xzf /tmp/{arch_name} -C \
                /data/web_static/releases/{arch_wext}/")
        run(f"rm /tmp/{arch_name}")
        run(f"mv /data/web_static/releases/{arch_wext}/web_static/* \
                /data/web_static/releases/{arch_wext}/")
        run(f"rm -rf /data/web_static/releases\
                /{arch_wext}/web_static")
        run(f"rm -rf /data/web_static/current")
        run(f"ln -s /data/web_static/releases/{arch_wext}/ \
                /data/web_static/current")

        return True

    except Exception as e:
        return False
