from fabric.api import local
from datetime import datetime

"""Fabric script that generates a .tgz archive"""


def do_pack():
    """Archive from the contents of the web_static folder"""

    local('mkdir -p versions')

    tm = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    arch_name = f"versions/web_static_{tm}.tgz"

    res = local(
            f"tar -cvzf {arch_name} web_static",
            capture=True
        )

    if res.failed:
        return None
    return arch_name
