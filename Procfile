web: python manage.py migrate --noinput && gunicorn liafe_project.wsgi --bind 0.0.0.0:$PORT --workers 2 --timeout 120
