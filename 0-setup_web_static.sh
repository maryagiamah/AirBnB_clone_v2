#!/usr/bin/env bash
# Sets up your web servers for the deployment of web_static
if ! dpkg -l | grep -q "^ii  nginx"
then
    sudo apt-get update
    sudo apt-get install nginx -y
fi

service nginx start
args="/data/
/data/web_static/
/data/web_static/releases/
/data/web_static/shared/
/data/web_static/releases/test/
"

for arg in $args
do
    if [ ! -e "$arg" ]
    then
          mkdir "$arg"
    fi
done

sudo su <<EOF
ln -sf /data/web_static/releases/test /data/web_static/current

echo "Hi there" > /data/web_static/releases/test/index.html

chown -R ubuntu:ubuntu /data/

sed -i '/server_name _;/a\\
        location /hbnb_static/ {\\
                alias /data/web_static/current/;\\
        }\\
' /etc/nginx/sites-enabled/default
EOF
