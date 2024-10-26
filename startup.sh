python3 manage.py migrate
python3 manage.py collectstatic && gunicorn -k uvicorn.workers.UvicornWorker websocket_demo.asgi:application