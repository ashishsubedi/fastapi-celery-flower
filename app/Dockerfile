FROM python:3.9.5-slim-buster

RUN adduser python
USER python

WORKDIR /usr/src/app


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip

COPY --chown=python:python ./requirements.txt requirements.txt
RUN pip install --user -r requirements.txt

ENV PATH="/home/python/.local/bin:${PATH}"
# copy project
COPY --chown=python:python . .

WORKDIR /usr/src