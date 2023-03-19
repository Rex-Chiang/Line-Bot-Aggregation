#!/bin/bash
celery -A config worker -B -l DEBUG & gunicorn -c gunicorn.conf.py config.wsgi --log-level DEBUG --timeout 300 --keep-alive 50