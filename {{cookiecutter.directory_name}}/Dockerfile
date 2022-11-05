FROM python:3.8

ENV PYTHONUNBUFFERED=1

# Env vars
ENV DJANGO_SETTINGS_MODULE ${DJANGO_SETTINGS_MODULE}
# Config secrets
ENV SECRET_KEY ${SECRET_KEY}
# database secrets
ENV DB_NAME ${DB_NAME}
ENV DB_HOST ${DB_HOST}
ENV DB_PORT ${DB_PORT}
ENV DB_USER ${POSTGRES_USER}
ENV DB_PASSWORD ${POSTGRES_PASSWORD}

WORKDIR /code

RUN pip install --upgrade pip
COPY requirements/* /code/requirements/
RUN pip install -r requirements/production.txt
COPY . /code/
RUN mkdir /code/logs