#!/bin/sh
set -e

echo "[entrypoint] Iniciando setup do banco..."
python seed.py
echo "[entrypoint] Setup concluído. Iniciando gunicorn..."

exec gunicorn --bind 0.0.0.0:5000 --workers 2 --threads 4 run:app