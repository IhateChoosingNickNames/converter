FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

LABEL author='Larkin Michael'

CMD ["gunicorn", "root.wsgi:application", "--bind", "0:8000" ]