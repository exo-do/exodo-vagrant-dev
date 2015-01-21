#!/usr/bin/env bash

# Descarga e instala todo lo que necesitamos
apt-get update
apt-get install -y python-software-properties python g++ make imagemagick git python-pip
add-apt-repository -y ppa:chris-lea/node.js

# Fumada para instalar mongo
apt-key adv --keyserver keyserver.ubuntu.com --recv 7F0CEB10
echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' | sudo tee /etc/apt/sources.list.d/mongodb.list
apt-get update

apt-get -y install nodejs mongodb-org 

# Actualiza pip e instala las dependencias para python
pip install -U pip
pip install -U requests

# Instala repositorios en los que desarrollamos
python /vagrant/nodebb_installer.py

