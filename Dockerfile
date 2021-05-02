FROM python:3.8.1

COPY . /chaos
WORKDIR /chaos

ENV YOTTA_ML3_CONFIGURATION_PATH=/secret/config.yml

RUN apt-get update

RUN pip install -r requirements.txt
RUN pip install -e ./


ENV FLASK_PORT=5000
EXPOSE ${FLASK_PORT}

CMD ["gunicorn", "chaos.application.server:app", "-b", "0.0.0.0:5000"]