FROM python:3.6.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
COPY . /app/
WORKDIR /app
RUN pip install -r requirements.txt
RUN rm -rf static
RUN python manage.py collectstatic --noinput