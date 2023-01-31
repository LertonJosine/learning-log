FROM python:3.11.1-slim-bullseye

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /learning_log

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .