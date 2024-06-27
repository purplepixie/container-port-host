FROM python:latest

WORKDIR /app

RUN pip3 install Flask

COPY ./src .

CMD [ "python3", "app.py" ]