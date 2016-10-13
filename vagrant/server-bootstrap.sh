#!/usr/bin/env bash
apt-get update
apt-get install -y python-pip
pip install -U pip setuptools
cd /home/vagrant/src
sudo pip install -r requirements.txt
python manage.py migrate
python manage.py populate


# server
ssh-keygen -t rsa -b 4096 -C "mail@rafaelferreira.pt"
cd .ssh
cat id_rsa.pub
cd ~
git clone git@github.com:rafaelferreirapt/rfid.git
cd rfid/src
sudo pip install -r requirements.txt
#python manage.py migrate
#python manage.py populate
