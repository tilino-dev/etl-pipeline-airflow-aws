# etl-pipeline-airflow-aws

Simple Airflow-driven ETL pipeline that downloads NYC taxi data, transforms it, and loads to Postgres.

## Project Description

**ETL Pipeline with Airflow and AWS** is a data engineering project that demonstrates how to build a scalable, automated Extract-Transform-Load (ETL) workflow using Apache Airflow, PostgreSQL, and AWS services.

### What does this project do?

- **Extracts data** from a source system or files (like CSVs or APIs).  
- **Transforms the data** by cleaning, filtering, and reshaping it to make it useful and consistent.  
- **Loads the transformed data** into a PostgreSQL database for easy querying and analysis.  
- **Automates the entire pipeline** with Apache Airflow, which schedules and monitors each step as a Directed Acyclic Graph (DAG).  
- **Uses AWS services** (like S3 or RDS) to store raw data or host the database, showcasing how cloud platforms fit into modern data workflows.  

### Key features

- Modular DAGs written in Python, making it easy to customize and extend.  
- Connection management using environment variables (`DB_CONN`) to securely handle database credentials without hardcoding them in scripts.  
- Example Docker Compose setup for running Airflow and PostgreSQL locally, simplifying development and testing.  
- Clear separation between extract, transform, and load stages for maintainability and scalability.  

### Why is this project useful?

Data pipelines are the backbone of any data-driven organization. Automating data extraction, transformation, and loading saves time, reduces errors, and makes data available faster. This project serves as a practical example for building reliable pipelines using popular open-source tools and cloud services. It’s ideal for anyone looking to understand ETL concepts, Airflow orchestration, and cloud integration.


## Run locally (simplified)
- Install requirements: pip install -r requirements.txt
- Set DB_CONN env var or edit scripts/load.py
- Run python scripts/extract.py
- Run python scripts/transform.py
- Run python scripts/load.py

To run with Airflow see docker-compose.yaml
