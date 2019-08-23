FROM python:3.7.3

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV LANG en_US.UTF-8
ENV PYTHONIOENCODING utf_8

RUN apt update && \
  apt upgrade -y && \
  apt install -y sass

RUN pip install mysqlclient && \
    pip install gunicorn

RUN git clone https://github.com/yangzhenweiq/elite-wagtail.git /elite-wagtail
WORKDIR /elite-wagtail/elite_wagtail

RUN pip install -r requirements.txt

RUN sass --update elite_wagtail/static/sass:elite_wagtail/static/css -E utf-8

EXPOSE 8000
CMD gunicorn --workers=2 --name wagtail --bind=0.0.0.0:8000 --max-requests=1000 elite_wagtail.wsgi:application

