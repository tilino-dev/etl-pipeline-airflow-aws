import requests
from pathlib import Path

def extract():
    Path('data').mkdir(exist_ok=True)
    url = 'https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2023-01.csv'
    out = Path('data/yellow_2023_01.csv')
    if out.exists():
        print('Already downloaded')
        return
    r = requests.get(url, stream=True)
    r.raise_for_status()
    with open(out, 'wb') as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)
    print('Downloaded to', out)