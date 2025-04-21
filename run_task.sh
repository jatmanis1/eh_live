#!/bin/bash

read -p "Enter a number (1-5): " choice

case $choice in
  1)
    cd ./frontend
    npm install
    npm run dev
    ;;
  2)
    cd ./backend
    python3 run.py
    ;;
  3)
    cd ./backend
    redis-server --port 6369
    ;;
  4)
    cd ./backend
    celery -A run.celery worker --loglevel=info
    ;;
  5)
    cd ./backend
    celery -A run.celery beat --loglevel=info
    ;;
  *)
    echo "Invalid option. Enter a number from 1 to 5."
    ;;
esac
