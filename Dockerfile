FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=0
ENV DEBUG 0
RUN mkdir /code
WORKDIR /code
COPY . /code/
RUN pip install --upgrade pip
RUN pip install -r /code/requirements.txt
RUN python manage.py collectstatic
RUN python manage.py makemigrations && python manage.py migrate
CMD gunicorn user_registration.wsgi:application --bind 0.0.0.0:$PORT