import random
import matplotlib.pyplot as plt 

### modify these values ###
capital = 100 # total money you have
number_of_trades = 214 # amount of trades you've taken in total
number_of_tests = 500 # repeat tests for higher accuracy. 

average_profit = 0.059 # average profit % expressed in decimal
average_loss = 0.0362 # average loss % expressed in decimal, so 0.1 = 10%
win_rate = 57 # % win rate of trades 



### determines overall returns based on % of capital risked ###
def possibilities(win_rate, average_loss, average_profit, capital_risk):
    total = []
    average = 0
    # Creates ton of tests, to find overall remaining capital 
    for i in range(number_of_tests):
        returns = [capital]
        for i in range(number_of_trades):
            wl = random.randrange(0,100)
            if wl <= win_rate:
                balance = (returns[-1] * ((capital_risk/100)*average_profit)) + returns[-1]
                returns.append(balance)
            elif wl > win_rate:
                balance = returns[-1] - ((returns[-1] * (capital_risk/100)*average_loss))
                returns.append(balance)
        total.append(returns)
    # Determines average remaining capital of all tests. 
    
    for x in range(number_of_tests):
        average += total[x][-1]
    average = average/number_of_tests
    return average

account_values = []
# Main function, tests function with different risk % of capital
for x in range(1, 100): # Always risk less than 25% on a single trade
    y = possibilities(win_rate, average_loss, average_profit, x)
    account_values.append(y)
print(account_values)    
# determine best risk % of capital
plt.plot(account_values)
best = max(account_values)
print('Optimal performance is '+ str(best) + ' at portfolio sizing ' + str(account_values.index(best)+1) + '% on a single trade')
