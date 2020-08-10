from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import requests
import plotly.offline as pyo
import plotly.graph_objects as go

def get_symbol (symbol):
    url = f'http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={symbol}&region=1&lang=en'
    result = requests.get(url).json()
    for x in result['ResultSet']['Result']:
        if x['symbol'] == symbol:
            return x['name']

def dateConversion (date):
    return datetime.strftime(date,'%Y-%m-%d')

start_date = input("Start date (YYYY-MM-DD): ")
start_date = datetime.strptime(start_date, '%Y-%m-%d')
compact_data_date = datetime.today() - timedelta(days = 100)

if start_date > (compact_data_date):
    key_data = 'compact'
else:
    key_data = 'full'

ts = TimeSeries(key = 'CDJRUJTR7IWQKE99', output_format = 'pandas')

stock = input("Add the first ticker: ").upper()
stock2 = input("Add the second ticker: ").upper()

company = get_symbol(stock)
company2 = get_symbol(stock2)

# outputsize: The size of the call (compact = 100, full = all)
data, meta_data = ts.get_daily(stock, outputsize = key_data)
data2, meta_data = ts.get_daily(stock2, outputsize = key_data)

first_date = data.tail(1).index[0]
first_date2 = data2.tail(1).index[0]

if first_date != first_date2 or max(first_date, first_date2) > start_date:
    start_date = max(first_date, first_date2, start_date)

data = data[data.index >= pd.to_datetime(start_date)]
data2 = data2[data2.index >= pd.to_datetime(start_date)]

first_val = data['4. close'][-1]
first_val_2 = data2['4. close'][-1]

a = data['4. close'].mul(100).div(first_val)
b = data2['4. close'].mul(100).div(first_val_2)

trace_0 = go.Scatter(x = data.index, y = a,
                     mode = 'lines', name = company)

trace_1 = go.Scatter(x = data2.index, y = b,
                     mode = 'lines', name = company2)

data = [trace_0, trace_1]

layout = go.Layout(title=f'Comparison between {company} and {company2}, starting from {dateConversion(start_date)}.',
                   hovermode = 'closest')

fig = go.Figure(data = data, layout = layout)
pyo.plot(fig, filename = 'stock_comparison.html')

