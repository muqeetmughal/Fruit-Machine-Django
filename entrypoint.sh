#Run migrations
python manage.py migrate

#run tests
# python manage.py test

# run collect statics
python manage.py collectstatic

echo 'COLLECT STAIIC DONE ********'
# Start server
# python manage.py runserver 0.0.0.0:$PORT
gunicorn core.wsgi:application --bind 0.0.0.0:8100