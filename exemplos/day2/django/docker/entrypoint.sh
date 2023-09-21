#!/usr/bin/env bash

set -e

python manage.py migrate --noinput

#echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python3 manage.py shell

python -m gunicorn -c python:djblog.gunicorn djblog.wsgi


$@
