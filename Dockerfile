FROM python:3.8.1

COPY . /src
WORKDIR /src

ENV YOTTA_ML3_CONFIGURATION_PATH=/secret/config.yml

RUN apt-get update

RUN pip install -r requirements.txt
RUN pip install -e ./


ENV API_PORT=5000
EXPOSE ${API_PORT}

<<<<<<< HEAD
CMD ["python", "src/application/server.py"]
=======
CMD ["gunicorn", "src.application.server:app", "-b", "0.0.0.0:5000"]
>>>>>>> 3169d7d7e8160bd41164ded7211f53a46d4f916d
