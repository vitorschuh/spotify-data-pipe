airflow-folders:
	python3 pull.py

airflow-init:
	docker compose up airflow-init -d

run:
	docker compose up -d

disarm:
	docker compose down -v

healthy-check:
	docker container ls