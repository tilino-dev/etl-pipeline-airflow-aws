from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import os

DEFAULT_ARGS = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(dag_id='nyc_taxi_daily', start_date=datetime(2024,1,1), schedule_interval='@daily', default_args=DEFAULT_ARGS, catchup=False) as dag:
    extract = PythonOperator(
        task_id='extract_csv',
        python_callable=lambda: __import__('scripts.extract').extract()
    )

    transform = PythonOperator(
        task_id='transform',
        python_callable=lambda: __import__('scripts.transform').transform()
    )

    load = PythonOperator(
        task_id='load',
        python_callable=lambda: __import__('scripts.load').load()
    )

    extract >> transform >> load