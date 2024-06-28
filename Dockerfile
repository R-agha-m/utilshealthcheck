FROM python:3.11

ENV PYTHONUNBUFFERED 1

WORKDIR /app

ENV PYTHONPATH /app

COPY . .

RUN apt-get update && \
    pip install --no-cache-dir -r requirements_for_linux.txt

CMD ["python", "."]
