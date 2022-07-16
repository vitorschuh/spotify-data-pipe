FROM apache/airflow:2.3.3

COPY requirements.txt .

USER root
RUN apt-get update
USER airflow

RUN python -m pip install --no-cache-dir --upgrade pip \
    python -m pip install --force --no-cache-dir -r requirements.txt