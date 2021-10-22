FROM python:3.9.7-alpine3.14

RUN mkdir -p /app

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 4000

ENTRYPOINT sh