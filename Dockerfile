FROM python:3.9.13
WORKDIR /app
COPY ./requirements/
RUN pip install -r base.txt
RUN pip install -r prod.txt

COPY . .
EXPOSE 10000
CMD ["sh", "-c", "python manage.py migrate && python manage.py collectstatic --noinput && gunicorn config.wsgi:application --bind --workers 2 --theards 4"]