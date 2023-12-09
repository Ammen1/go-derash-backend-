#!/bin/bash

SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-"hello@goderash.com"}
cd /app/

/opt/env/bin/python manage.py migrate --noinput
/opt/env/bin/python manage.py createsuperuser --email $SUPERUSER_EMAIL --noinput || true
