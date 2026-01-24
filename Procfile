web: sh -c "python manage.py migrate --noinput && gunicorn vitta.wsgi:application --bind 0.0.0.0:$PORT"
