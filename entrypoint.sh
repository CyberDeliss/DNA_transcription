#!/bin/sh

echo "Waiting for postgres..."

#while ! nc -z 127.0.0.1 5432; do
#  sleep 0.1
#done

sleep 10


echo "PostgreSQL started"


uvicorn main:app --forwarded-allow-ips='*' --host 0.0.0.0 --port 8000

exec "$@"