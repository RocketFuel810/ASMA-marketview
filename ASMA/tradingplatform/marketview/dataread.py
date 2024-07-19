
import pandas_datareader.av.time_series as ts
import pandas_datareader.nasdaq_trader as nt
import requests
import json
import numpy as np
import pandas as pd


class Stocks:

    def StockFrame():
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'
        r = requests.get(url)
        data = r.json()
        times = [key for key in data["Time Series (5min)"].keys()]
        prices = [data["Time Series (5min)"][time] for time in times]
                
        opens = [inst['1. open'] for inst in prices]
        highs = [inst['2. high'] for inst in prices]
        lows = [inst['3. low'] for inst in prices]
        closes = [inst['4. close'] for inst in prices]
        print(json.dumps(prices))
    
    def News():
        url = "https://www.alphavantage.co/query?function=NEWS_SENTIMENT&apikey=TRL8S38I56MBYQ4D"
        r = requests.get(url)
        return r.json()
    
    StockFrame()