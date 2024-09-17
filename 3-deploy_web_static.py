#!/usr/bin/python3
"""Creates and distributes an archive to your web servers"""

from fabric import *

env.hosts = ['54.175.134.91', '100.25.104.180']
env.user = 'ubuntu'

do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy


def deploy():
    """Deploy"""
    res = do_pack()

    if res is None:
        return False
    else:
        return do_deploy(res)
