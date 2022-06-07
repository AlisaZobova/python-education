FROM python:3.8-slim-buster

WORKDIR /de_intro_1

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD [ "python3", "app.py"]
