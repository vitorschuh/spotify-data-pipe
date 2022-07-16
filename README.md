![Airflow](https://img.shields.io/badge/Airflow-ffffff?style=for-the-badge&logo=Apache%20Airflow&logoColor=grey)
![Spotify](https://img.shields.io/badge/Spotify-1ED760?style=for-the-badge&logo=spotify&logoColor=white)

# Spotify data ETL

This repo presents a self-authored project from a Spotify data pipeline. The idea is to create an Airflow with Docker instance, extract raw data from the Spotity API using a personal account, get data that makes sense using in-code transforms and load the final dataset into a Postgres database. The aim is to practice data engineering skills like API consumption, container programming, and task scheduling and orchestration.

![alt text](https://github.com/vitorschuh/spotify-data-pipe/blob/main/img/data_landscape.png)

## Requirements
- Python
- Docker
- Spotify account (not premium required)


## Skeleton

```
|-- dags
    |-- spotify
        |-- custom_dags
            -- dags --
        |-- etl
            -- etl scripts --
            |-- utils
                -- etl utils --
|-- data
    |-- raw
    |-- curated
|-- logs
|-- plugins
-- setup scripts --
```

## Environment
To prepare environment the `example.env` file can be used. the variables that demand attention or explanation are:
| Variable | Description |
| ----- | ----------- |
| AIRFLOW_UID | Airflow user id |
| CLIENT_ID | Spotify client id |
| CLIENT_SECRET | Spotify client secret |
 
On Linux, the right Airflow user id can be obtained with `$(id -u)`. For other OS the 50000 id can be placed manually on this variable. To get Spotify client and secret credentials access your dashboard from  [Spotify for Developers](https://developer.spotify.com/dashboard/), go to “create an app”, generate fresh tokens and set the values in your environment file.

## Run

To make Airflow directories structure:

```
$ python3 pull.py 
```

To initialize Airflow services:

```
$ docker compose up airflow-init -d
```

To up full Airflow services and Postgres database:

```
$ docker compose up -d
```

To disarm compose and exclude associated volumes and networks:

```
$ docker compose down -v
```
