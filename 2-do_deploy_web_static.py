#!/usr/bin/python3
from fabric.api import env, put, sudo
import os

"""distributes an archive to your web servers"""


def do_deploy(archive_path):
    if not os.path.exists(archive_path):
        return False
    try:
        env.hosts = ['ubuntu@54.175.134.91', 'ubuntu@100.25.104.180']
        env.key_filename = '~/.ssh/school'
        arch_name = archive_path.split('/')[-1]
        arch_wext = arch_name.split('.')[0]

        put(archive_path, f"/tmp/{arch_name}")
        sudo(f"mkdir -p /data/web_static/releases/{arch_wext}/")
        sudo(f"tar -xzf /tmp/{arch_name} \
                -C /data/web_static/releases/{arch_wext}/")
        sudo(f"rm /tmp/{arch_name}")
        sudo(f"mv /data/web_static/releases/{arch_wext}/web_static/* \
                /data/web_static/releases/{arch_wext}/")
        sudo(f"rm -rf /data/web_static/releases/{arch_wext}/web_static")
        sudo(f"rm -rf /data/web_static/current")
        sudo(f"ln -s /data/web_static/releases/{arch_wext} \
                /data/web_static/current")
        return True
    except Exception as e:
        return False
