FROM python:3.9.6-alpine

EXPOSE 8080

COPY ./ /app

COPY requirements.txt /app

VOLUME [ "/app" ]

WORKDIR /app

RUN apk update
RUN apk add git
RUN apk add python3-dev
RUN pip install -r requirements.txt
RUN pip install --upgrade pip
RUN apk add gcc
RUN apk add --no-cache libressl-dev musl-dev libffi-dev

CMD ["python", "-m", "src.main"]
