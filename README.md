# etl-pipeline-airflow-aws

Simple Airflow-driven ETL pipeline that downloads NYC taxi data, transforms it, and loads to Postgres.

## Project Description

**ETL Pipeline with Airflow and PostgreSQL** is a data engineering project that demonstrates how to build a scalable, automated Extract-Transform-Load (ETL) workflow using Apache Airflow and PostgreSQL.

### What does this project do?

- **Extracts data** from source files or APIs.  
- **Transforms the data** by cleaning, filtering, and reshaping it to make it consistent and analysis-ready.  
- **Loads the transformed data** into a PostgreSQL database for querying and reporting.  
- **Automates the pipeline** with Apache Airflow, scheduling and monitoring the workflow as a Directed Acyclic Graph (DAG).  
- Uses **environment variables** (like `DB_CONN`) to securely manage the database connection without hardcoding sensitive information.

### Key features

- Modular and clear DAGs written in Python, easy to customize.  
- Local development support with a Docker Compose setup that runs Airflow and PostgreSQL containers.  
- Clean separation of extract, transform, and load tasks for maintainability.

### Why is this project useful?

Automating ETL pipelines ensures data is processed accurately and delivered on time. This project helps you understand how to use Airflow to orchestrate data workflows and how to connect and load data into PostgreSQL databases, a common setup in many companies.


## Run locally (simplified)
- Install requirements: pip install -r requirements.txt
- Set DB_CONN env var or edit scripts/load.py
- Run python scripts/extract.py
- Run python scripts/transform.py
- Run python scripts/load.py

To run with Airflow see docker-compose.yaml
