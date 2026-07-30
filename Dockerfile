FROM python:3.9.13
WORKDIR /app
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 10000
CMD ["gunicorn", "config.asgi:application", "--bind", "[IP_ADDRESS]:8000"]