FROM python:3.10-alpine
RUN apk add postgresql-dev gcc python3-dev musl-dev
WORKDIR /code
COPY requirements.txt requirements.txt
RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --no-cache --virtual .build-deps build-base linux-headers
RUN pip install -r requirements.txt
RUN apk del .build-deps
RUN pip install gunicorn
COPY . .
CMD ["gunicorn" ,"main.wsgi" ,"-w" ,"2" ,"--bind",":8000","--reload"]
