FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=0
ENV DEBUG 0
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
CMD gunicorn user_registration.wsgi:application --bind 0.0.0.0:$PORT