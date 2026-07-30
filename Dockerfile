FROM python:3.9.13
WORKDIR /app
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 10000
CMD "gunicorn porifolio_site.asgi:application  --workers 2 --threads 4 --timeout 120"