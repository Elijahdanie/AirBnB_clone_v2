#!/usr/bin/env bash
# This shell script configures folders for deployment

sudo apt-get update
sudo apt-get install -y nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo chown -Rh ubuntu:ubuntu /data/
echo "This is the index" >> /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo sed -i "/server_name _;/a location /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n" /etc/nginx/sites-available/default
sudo service nginx restart
