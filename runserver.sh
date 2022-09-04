#!/bin/bash
celery -A config worker -B -l INFO & gunicorn -c gunicorn.conf.py config.wsgi  --timeout 300 --keep-alive 50