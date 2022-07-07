FROM python:3.8-slim-buster

WORKDIR /py_flask_mongo

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "-u", "waitress_server.py"]

