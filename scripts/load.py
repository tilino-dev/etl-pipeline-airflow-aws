import psycopg2
import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path
import os

def load():
    engine = create_engine(os.getenv('DB_CONN', 'postgresql+psycopg2://airflow:airflow@localhost:5432/airflow'))
    df = pd.read_parquet('data/yellow_2023_01_transformed.parquet')
    df.to_sql('yellow_trips', engine, if_exists='replace', index=False)
    print('Loaded to Postgres')