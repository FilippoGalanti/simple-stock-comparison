# https://github.com/RomelTorres/alpha_vantage

from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import requests

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
    print(f'First available date: {max(first_date, first_date2, start_date)}')
    start_date = max(first_date, first_date2, start_date)

data = data[data.index >= pd.to_datetime(start_date)]
data2 = data2[data2.index >= pd.to_datetime(start_date)]

first_val = data['4. close'][-1]
first_val_2 = data2['4. close'][-1]
last_val = data['4. close'][0]
last_val2 = data2['4. close'][0]

a = data['4. close'].mul(100).div(first_val)
b = data2['4. close'].mul(100).div(first_val_2)

print(f'{company} start value ${first_val:,.2f} on {dateConversion(start_date)}. End value ${last_val:,.2f} on {dateConversion(data.head(1).index[0])}.')
print(f'{company2} start value ${first_val_2:,.2f} on {dateConversion(start_date)}. End value ${last_val2:,.2f} on {dateConversion(data2.head(1).index[0])}.')

a.plot.line(label = company)
b.plot.line(label = company2)
plt.legend(loc = 'best', fontsize = 'small')
plt.show()