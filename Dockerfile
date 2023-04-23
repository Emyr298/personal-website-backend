FROM python:3.10.8-alpine

ARG DJANGO_KEY
ARG DATABASE_URL
ARG ENVIRONMENT

ENV DJANGO_KEY ${DJANGO_KEY}
ENV DATABASE_URL ${DATABASE_URL}
ENV ENVIRONMENT ${ENVIRONMENT}

WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt --no-cache-dir
COPY . /app

EXPOSE 8000
CMD "python manage.py migrate && python manage.py collectstatic && python manage.py runserver 0.0.0.0:8000"
