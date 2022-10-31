FROM python:3.11.0-alpine3.16
RUN apk add postgresql-dev gcc python3-dev musl-dev libev-dev  jpeg-dev zlib-dev
WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install bjoern
COPY . .
CMD ["python","serve.py"]
