import os


def create_airflow_folders() -> None:
    os.makedirs(name="./dags", exist_ok=False)
    os.makedirs(name="./logs", exist_ok=False)
    os.makedirs(name="./plugins", exist_ok=False)

if __name__ == "__main__":
    create_airflow_folders()
