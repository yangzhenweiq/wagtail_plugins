FROM python:3.7.3

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV LANG en_US.UTF-8
ENV PYTHONIOENCODING utf_8

RUN apt update && \
    apt install sass

RUN pip install mysqlclient && \
    pip install gunicorn && \
    pip install gevent

RUN git clone https://github.com/yangzhenweiq/elite-wagtail.git /elite-wagtail
WORKDIR /elite-wagtail/elite_wagtail

RUN pip install -r requirements.txt

