python3 manage.py migrate
python3 manage.py collectstatic
python3 -m gunicorn --workers 2 websocket_demo.asgi:application -k uvicorn_worker.UvicornWorker