FROM python:3.8.5

# Install packages to complie
RUN apt install make gcc g++ libc-dev

WORKDIR /code

# Install needed packages
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .

LABEL maintainer="Muqeet Mughal <muqeetmughal786@gmail.com>"

# Run server
# CMD python manage.py runserver 0.0.0.0:8000
# CMD gunicorn -c gunicorn.py "core.wsgi:application"
# ENTRYPOINT [ "/entrypoint.sh" ]
