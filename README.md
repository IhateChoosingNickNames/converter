# Converter
Simple API for conversion currency


Used technologies:
-
    - python 3.11
    - django 4.2
    - djangorestframework 3.14
    - python-dotenv 0.21.1
    - Docker 20.10.22
    - Poetry 1.4.0
    - Requests 2.31.0

# Launch instructions:


## Set enviroment:
Fill go to /infra folder and create and fill .env file according to shown in .env.sample file.
- SECRET_KEY=... # secret key from Django project
- CONTAINER_NAME=backend # name of your backend container
- API_KEY=... - key for http://api.exchangeratesapi.io


## Install docker compose and run:
    docker-compose up -d --build
For now app is available at localhost


If you'll need any *manage.py* commands then you'll want to use prefix:

    docker-compose exec backend python manage.py *comand*


Examples requests:
-
    - GET your_url/api/rates/?from=RUB&to=USD&value=127

Examples of responses:
-
    - GET {
    "result": 1.2700629259007803
    }

### Project author:

Larkin Mikhail
https://github.com/IhateChoosingNickNames