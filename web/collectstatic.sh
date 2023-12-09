#!/bin/bash
cd /app/
/opt/env/bin/python manage.py collectstatic --noinput
