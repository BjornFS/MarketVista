import pandas as pd
import plotly
import yfinance as yf
from OMXC25 import FetchIndex

ticker = FetchIndex()

tickers = []
deltas = []
sectors =[]
market_caps = []

for n in ticker:
    try:
        ## create Ticker object
        stock = yf.Ticker(n)
        tickers.append(n)

        ## download info
        info = stock.info
        ## add print statement to ensure code is running
        print(n + ' downloading...')

        ## download sector
        sectors.append(info['sector'])

        ## download daily stock prices for last 30 days
        hist = stock.history('30d')

        ## calculate change in stock price (from a trading day ago)
        deltas.append((hist['Close'][1]-hist['Close'][0])/hist['Close'][0])

        ## calculate market cap
        market_caps.append(info['sharesOutstanding'] * info['previousClose'])

        ## add print statement to ensure code is running
        print(n + ' downloaded')        
    except Exception as e:
        print(e)

df = pd.DataFrame({'ticker':tickers,
                  'sector': sectors,
                  'delta': deltas,
                  'market_cap': market_caps,
                  })

color_bin = [-1,-0.02,-0.01,0, 0.01, 0.02,1]
df['colors'] = pd.cut(df['delta'], bins=color_bin, labels=['red','indianred','lightpink','lightgreen','lime','green'])

import plotly.express as px
fig = px.treemap(df, path=[px.Constant("all"), 'sector','ticker'], 
                values = 'market_cap', 
                color='colors',
                color_discrete_map ={'(?)':'#262931', 'red':'red', 'indianred':'indianred','lightpink':'lightpink', 'lightgreen':'lightgreen','lime':'lime','green':'green'}, 
                hover_data = {'delta':':.2p'}, 
                color_continuous_scale='colors')

fig.show()