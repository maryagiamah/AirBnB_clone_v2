#!/usr/bin/python3
from fabric.api import env, put, run
from os.path import exists

# Define your servers' IPs
env.hosts = ['100.25.104.180', '54.175.134.91']


def do_deploy(archive_path):
    """Distributes an archive to web servers"""

    # Check if archive exists
    if not exists(archive_path):
        return False

    try:
        # Extract filename and folder name
        filename = archive_path.split('/')[-1]
        no_ext = filename.split('.')[0]
        release_path = f"/data/web_static/releases/{no_ext}"

        # Upload the archive to the /tmp/ directory
        put(archive_path, '/tmp/')

        # Create the release folder
        run(f'mkdir -p {release_path}/')

        # Uncompress the archive into the release folder
        run(f'tar -xzf /tmp/{filename} -C {release_path}/')

        # Remove the archive from the server
        run(f'rm /tmp/{filename}')

        # Move the extracted files out of the web_static folder
        run(f'mv {release_path}/web_static/* {release_path}/')

        # Remove the now-empty web_static folder
        run(f'rm -rf {release_path}/web_static')

        # Remove the old symbolic link
        run('rm -rf /data/web_static/current')

        # Create a new symbolic link
        run(f'ln -s {release_path} /data/web_static/current')

        return True
    except Exception:
        return False
