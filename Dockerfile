FROM python:3.8.1

COPY . /src
WORKDIR /src

ENV YOTTA_ML3_CONFIGURATION_PATH=/secret/config.yml

RUN apt-get update

RUN pip install -r requirements.txt
RUN pip install -e ./


ENV API_PORT=5000
EXPOSE ${API_PORT}

CMD ["python", "src/application/server.py"]
