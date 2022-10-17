# phoenix-backend
Django Rest Backend

# How to Set up Locally:
- Clone the repo
- create a .env file with these values:
    - DJANGO_SECRET_KEY -> your django secret key
    - POSTGRES_USER -> your postgres user
    - POSTGRES_PASSWORD -> your postgres password
    - POSTGRES_DB -> your postgres database
    - POSTGRES_HOST -> your postgres host
    - POSTGRES_PORT -> your postgres port
    - env -> dev or prod depending what you want

- create virtualenv using venv. Activate it.
- run `pip install -r requirements.txt`
- run `python manage.py migrate` [ For First Time ]
- run `python manage.py collectstatic` [For the first time]
- run `python manage.py runserver` app would be running on `localhost:8000`

## For Docker
If you don't want to set up your own postgres
Use the docker-compose provided already by :
- Alternatively if you want to use docker use , docker-compose up -d
- open a shell into the `web` service
- run `python manage.py migrate` [ For First Time ]
- run `python manage.py collectstatic` [For the first time]
Service will be running on `localhost:8000`
