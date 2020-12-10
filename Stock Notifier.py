import pandas as pd
import numpy as np
import yfinance as yf
import datetime as dt
from datetime import timedelta
from pandas_datareader import data as pdr
# Work around Yahoo Finance
yf.pdr_override()
# dict of stocks and notif points 
stocks = {'amzn':3050, 'sq':190, 'bynd':133, 'ba':200, 'rkt':19.5, 'lmnd':64, 'crsr':35, 'ayx':115, 
         'amd':82, 'u':130, 'aal':14, 'etsy':140, 'pltr':20, 'spce':24.5, 'fsly':80, 'chgg':67,
         'chwy':64, 'pins':60, 'net':65, 'apps':36}
# Get current time
now = dt.datetime.now()
# Get yesterdays date
yesterday = now + timedelta(-2)
for ticker in stocks.keys(): 
    df=pdr.get_data_yahoo(ticker,yesterday,now)
    # Gets todays and yesterdays prices 
    today = df['Close'][-1]
    yday = df['Close'][0]
    # checks for break through 
    if today < stocks[ticker] < yday:
        print("!!-----------!!\n")
        print("Stock "+ str(ticker) + " is now below support level " + str(stocks[ticker])+'\n')
        print("!!-----------!!\n")
    # prints stock price and % change in price
    print("-----------"+str(ticker)+"-----------")
    print("Todays close: "+ str(today) + "\n" + "Yesterdays close: "+str(yday))
    print("% change in price: " + str(((today-yday)/yday)*100) + '%\n')
