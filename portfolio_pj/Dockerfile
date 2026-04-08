FROM python:3.10

ENV PYTHONUNBUFFERED 1

RUN mkdir /app
COPY . /app/
WORKDIR /app

RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput

CMD gunicorn portfolio_pj.wsgi -b 0.0.0.0:$PORT
