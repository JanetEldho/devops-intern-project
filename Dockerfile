FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install flask gunicorn

CMD ["gunicorn", "app:app", "-b", "0.0.0.0:5000"]