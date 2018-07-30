#!/usr/bin/env bash
# this script  sets up your web servers for the deployment of web_static
# update and install nginx
sudo apt-get -y update
sudo apt-get -y install nginx
# create folders
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
# create simple file to test
echo -e '<html>\n<head>\nHBnB</head>\n<body>\nHolberton School\n</body>\n</html>' | sudo tee /data/web_static/releases/test/index.html
# create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
# give ownership to the group and user
sudo chown -R ubuntu:ubuntu /data/
# creating alias
sudo sed -i "37i \\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n\n" /etc/nginx/sites-enabled/default
sudo service nginx restart
