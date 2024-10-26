python manage.py migrate
python manage.py collectstatic && gunicorn -k uvicorn.workers.UvicornWorker websocket_demo.asgi:application