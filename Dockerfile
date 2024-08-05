FROM python:3.11

ENV PYTHONUNBUFFERED 1

WORKDIR /app

ENV PYTHONPATH /app

COPY . .

RUN apt-get update
RUN pip install -r requirements-linux.txt  # --no-cache-dir

CMD ["python", "__main__.py"]
