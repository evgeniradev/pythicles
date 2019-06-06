FROM python:3.7.3-alpine
RUN apk upgrade
RUN apk add postgresql-dev gcc python3-dev musl-dev jpeg-dev zlib-dev
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
