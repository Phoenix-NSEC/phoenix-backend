FROM python:3.10-alpine
RUN apk add postgresql-dev gcc python3-dev musl-dev
WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install gunicorn
COPY . .
CMD ["gunicorn" ,"main.wsgi" ,"-w" ,"2" ,"--bind",":8000","--reload"]
