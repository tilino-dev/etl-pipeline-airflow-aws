# etl-pipeline-airflow-aws

Simple Airflow-driven ETL pipeline that downloads NYC taxi data, transforms it, and loads to Postgres.

## Run locally (simplified)
- Install requirements: pip install -r requirements.txt
- Set DB_CONN env var or edit scripts/load.py
- Run python scripts/extract.py
- Run python scripts/transform.py
- Run python scripts/load.py

To run with Airflow see docker-compose.yaml