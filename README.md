![Airflow](https://img.shields.io/badge/Airflow-ffffff?style=for-the-badge&logo=Apache%20Airflow&logoColor=grey)
![Spotify](https://img.shields.io/badge/Spotify-1ED760?style=for-the-badge&logo=spotify&logoColor=white)

# Spotify data ETL

This repo presents a self-authored project from a Spotify data pipeline. The idea is to create an Airflow with Docker instance, extract raw data from the Spotify API using a personal account, get data that makes sense using in-code transforms and load the final dataset into a Postgres database. The aim is to practice data engineering skills like API consumption, container programming, and task scheduling and orchestration.

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
To prepare environment the `example.env` file can be used. The variables that demand attention or explanation are:
| Variable | Description |
| ----- | ----------- |
| AIRFLOW_UID | Airflow user id |
| CLIENT_ID | Spotify client id |
| CLIENT_SECRET | Spotify client secret |
 
On linux, the right Airflow user id can be obtained with `$(id -u)`. For other OS the 50000 id can be placed manually on this variable. To get Spotify client and secret credentials access your dashboard from  [Spotify for Developers](https://developer.spotify.com/dashboard/), go to “create an app”, generate fresh tokens and set the values in your environment file.

## Run

To make Airflow directories structure:

```
$ make airflow-folders
```

To initialize Airflow services:

```
$ make airflow-init
```

To run full Airflow services and Postgres database:

```
$ make run
```

After that point, all Airflow services will be raised through compose. You can check the health of containers through:

```
$ make healthy-check
```

After that, you will be able to access the Airflow web server at <http://localhost/8080/home>. To run the ETL process just turn on the DAG and trigger it.

Finally, to see the result, run the Postgres container with:

```
$ docker exec -it <container_id> /bin/sh
$ psql --username <your_db_user>
```

and query the data with something like:

```sql
SELECT * FROM public."spotify-tracks";
```

To disarm compose and exclude associated volumes and networks:

```
$ make disarm
```

Note: all make "cmd" commands are made to run on macOS. To run on linux edit the Makefile replacing the occurrences of "docker compose" with "docker-compose".
