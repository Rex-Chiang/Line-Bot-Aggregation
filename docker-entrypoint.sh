#!/bin/bash

echo "Make swap file"
fallocate -l 256M /swapfile
chmod 0600 /swapfile
mkswap /swapfile
echo 10 > /proc/sys/vm/swappiness
swapon /swapfile
echo 1 > /proc/sys/vm/overcommit_memory

echo "Make migrations"
python3 manage.py makemigrations

echo "Apply database migrations"
python3 manage.py migrate

exec "$@"
