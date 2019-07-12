FROM python:3.7.3

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV LANG en_US.UTF-8
ENV PYTHONIOENCODING utf_8

RUN apt update

RUN pip install mysqlclient

RUN pip install wagtail

RUN wagtail start wagtail_site

WORKDIR /wagtail_site

RUN pip install -r requirements.txt

