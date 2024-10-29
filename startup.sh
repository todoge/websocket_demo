python manage.py migrate
#python manage.py collectstatic && gunicorn -k uvicorn.workers.UvicornWorker websocket_demo.asgi:application
python manage.py collectstatic
python -m gunicorn websocket_demo.wsgi:application --bind 0.0.0.0:8000
python -m daphne -b 0.0.0.0 -p 8089 websocket_demo.asgi:application
#python3 -m gunicorn websocket_demo.wsgi:application --bind 127.0.0.1:8000 --reload & daphne -b 127.0.0.1 -p 8089
#websocket_demo.asgi:application &
#python -m gunicorn websocket_demo.wsgi:application --bind 0.0.0.0:8000 --reload & daphne -b 0.0.0.0 -p 8089 app.asgi:application &