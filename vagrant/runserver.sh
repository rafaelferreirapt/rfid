#!/usr/bin/env bash
cd /home/vagrant/src
python manage.py makemigrations # only on the first time
python manage.py runserver 0.0.0.0:8000
