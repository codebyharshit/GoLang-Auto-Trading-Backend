import pandas as pd
from polygon import RESTClient

API_KEY = ''
SYMBOL = 'AAPL'

def fetch_data(symbol, api_key):
    client = RESTClient(api_key)
    aggs = []
    for a in client.list_aggs(ticker=symbol, multiplier=1, timespan="day", from_="2022-01-01", to="2023-06-13", limit=50000):
        aggs.append(a)
    
    data = {
        "timestamp": [a.timestamp for a in aggs],
        "open": [a.open for a in aggs],
        "high": [a.high for a in aggs],
        "low": [a.low for a in aggs],
        "close": [a.close for a in aggs],
        "volume": [a.volume for a in aggs],
    }
    return pd.DataFrame(data)

if __name__ == '__main__':
    df = fetch_data(SYMBOL, API_KEY)
    df.to_csv(f'data/{SYMBOL}_historical_data.csv')
    print(f'Data saved to data/{SYMBOL}_historical_data.csv')
