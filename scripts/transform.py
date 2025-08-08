import pandas as pd
from pathlib import Path

def transform():
    Path('data').mkdir(exist_ok=True)
    path = Path('data/yellow_2023_01.csv')
    df = pd.read_csv(path)
    # minimal transform: select a few columns and filter
    df2 = df[['tpep_pickup_datetime', 'tpep_dropoff_datetime', 'passenger_count', 'trip_distance', 'total_amount']].copy()
    df2.dropna(inplace=True)
    df2.to_parquet('data/yellow_2023_01_transformed.parquet', index=False)
    print('Wrote transformed parquet')