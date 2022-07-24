import requests
import pandas as pd

def FetchIndex():
    # Fetch index using request
    url = 'https://uk.finance.yahoo.com/quote/%5EOMXC25/components?p=%5EOMXC25'
    r = requests.get(url, headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})
    
    # convert to dataframe
    table = pd.read_html(r.text)
    index = table[0]

    # get tickers
    ticker = index["Symbol"].tolist()

    return ticker