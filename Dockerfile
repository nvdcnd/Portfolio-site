FROM python:3.9.13
WORKDIR /app

ENV PYTHONUNBUFFERED=1

COPY requirements/ ./requirements/
RUN pip install --no-cache-dir -r requirements/base.txt
RUN pip install --no-cache-dir -r requirements/prod.txt

COPY . .
EXPOSE 10000
CMD ["sh", "-c", "python manage.py migrate && python manage.py collectstatic --noinput && gunicorn config.wsgi:application --workers 2 --theards 4"]