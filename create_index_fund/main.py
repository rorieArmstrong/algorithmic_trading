# IMPORT MODULES
import pandas as pd;
import numpy as np;
import requests; 
import xlsxwriter;
import math;

#IMPORT API KEYS
from secrets import IEX_CLOUD_API_TOKEN

#IMPORT STOCKTICKERS
pd.DataFrame()
tickers = pd.read_csv(sp_500_stocks)

#MAKE API CALL
symbol='AAPL'
api_url = f'https://sandbox.iexapis.com/stable/stock/{symbol}/quote?token={IEX_CLOUD_API_TOKEN}'
data = requests.get(api_url).json()

#CREATE PANDA DATAFRAME FOR STOCK PRICES
my_columns = ['Ticker', 'Price','Market Capitalization', 'Number Of Shares to Buy']
final_dataframe = pd.DataFrame(columns = my_columns)
for symbol in stocks['Ticker']:
    api_url = f'https://sandbox.iexapis.com/stable/stock/{symbol}/quote?token={IEX_CLOUD_API_TOKEN}'
    data = requests.get(api_url).json()
    final_dataframe = final_dataframe.append(
                                        pd.Series([symbol, 
                                                   data['latestPrice'], 
                                                   data['marketCap'], 
                                                   'N/A'], 
                                                  index = my_columns), 
                                        ignore_index = True)
                                        
