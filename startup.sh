python manage.py migrate
python manage.py collectstatic
python -m daphne websocket_demo.asgi:application
python -m gunicorn --workers 2 websocket_demo.asgi:application -k uvicorn_worker.UvicornWorker