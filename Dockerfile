FROM python:3.9-alpine

RUN apk update \
    apk add bash \
    apd add python3 \
    apk add python3-dev \
    apk add py3-pip

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

CMD ["python", "app.py"]
