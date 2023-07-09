#!/usr/bin/env bash
# This sets up my web servers for the deployment of web_static
sudo apt-get -y update
sudo apt-get-y upgrade
sudo apt-get install -y nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>' > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '43i \\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx restart
