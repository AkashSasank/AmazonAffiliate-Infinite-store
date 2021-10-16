web: python manage.py collectstatic --noinput; bin/gunicorn_django --workers=4 --bind=0.0.0.0:$PORT core/settings.py
web: gunicorn core.wsgi --log-file -