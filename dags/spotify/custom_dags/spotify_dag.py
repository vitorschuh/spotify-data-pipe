import datetime
import os

from airflow import DAG
from airflow.models import Variable
from airflow.operators.python import PythonOperator
from spotify.etl.extract import extract
from spotify.etl.load import load
from spotify.etl.transform import transform

env = {
    "client_id": Variable.get("CLIENT_ID"),
    "client_secret": Variable.get("CLIENT_SECRET"),
    "raw_path": Variable.get("RAW_PATH"),
    "processed_path": Variable.get("CURATED_PATH"),
    "db_uri": Variable.get("DB_URI"),
    "db_user": Variable.get("DB_USER"),
    "db_password": Variable.get("DB_PASSWORD")
}


def create_data_folders() -> None:
    os.makedirs(name="./data/raw/", exist_ok=True)
    os.makedirs(name="./data/curated/", exist_ok=True)


with DAG(
    dag_id="spotify-dag",
    schedule_interval="40 4 * * *",
    start_date=datetime.datetime(2022, 7, 1),
    catchup=False,
    max_active_tasks=1,
    max_active_runs=1,
) as dag:

    create_data_folders()

    e = PythonOperator(
        task_id="extract_spotify_api",
        python_callable=extract,
        op_kwargs={
            "client_id": env["client_id"],
            "client_secret": env["client_secret"],
            "path": env["raw_path"],
        },
    )

    t = PythonOperator(
        task_id="transform",
        python_callable=transform,
        op_kwargs={
            "raw_path": env["raw_path"],
            "processed_path": env["processed_path"],
        },
    )

    l = PythonOperator(
        task_id="load_postgres",
        python_callable=load,
        op_kwargs={
            "path": env["processed_path"],
            "uri": env["db_uri"],
            "db": "postgres",
            "user": env["db_user"],
            "password": env["db_password"],
            "verbose": False
        },
    )

    e >> t >> l
