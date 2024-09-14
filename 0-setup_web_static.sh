#!/usr/bin/env bash

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

ln -sf /data/web_static/releases/test /data/web_static/current

sudo su <<EOF
echo "Hi there" > /data/web_static/releases/test/index.html

chown -R root:root /data/

sed -i '/server_name _;/a\\
        location /hbnb_static {\\
                alias /data/web_static/current;\\
        }\\
' /etc/nginx/sites-enabled/default
EOF
