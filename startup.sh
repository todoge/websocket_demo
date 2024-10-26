python manage.py migrate
python manage.py collectstatic && gunicorn --workers 2 websocket_demo.asgi:application -k uvicorn_worker.UvicornWorker