# Portfolio-Management-functions---Equities
'''
Has 3 functions:

Required inputs: Stop Loss, Entry, Current Price, Quantity of stocks purchased 

Averaging down: Gets user input regarding what price they want to average down to, and it returns the amount of stocks you need to purchase, with the stock being at its current market price for you to average down to your desired price. This also comes with a visual graph which plots out all other possible averaging down positions in correspondence to the amount of stocks you need to acquire to achieve that average entry. 

Break even: Calculates target price the stock needs to reach for you to offload {x amount} of stocks in order to have a risk free trade. This also displays a visual graph which plots all the other x amounts of stocks you can possibly offload in correspondence to what price the stock needs to reach for a risk free trade. 

Stock notifs: Which basically notifies you when a stock hits a pre determined price, it allows for both take profit and stop loss price points. 
'''
EDIT:
Updated version of stock notifs
- Allows for 2 dictionary data sets, 1 for swing trading / day trading, another for long terms. 
- Option to notify if it is within proximity i.e. 2% points away from the target average size level. 
- Plots out all the charts w/ indicators for all tickers which fit criteria 
- Indicators include Moving averages, Bollinger bands, Candle stick charts etc. 
