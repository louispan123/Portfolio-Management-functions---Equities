# Max capital per trade
max_risk = 3000
# How much less capital per additional risk level
reduction = 250
prices = [] # for storing average down prices 
risk_level = int(input("Risk level between 0-10 0 being least risk, 10 being most: "))
average_down = int(input("How many times your going to average down: "))
start_price = int(input("Whats your buying price: "))
prices.append(start_price)
while average_down > 0: 
    x = input("Whats your next averaging down price: ")
    prices.append(x)
    average_down -=1
# Works out how much capital we can utilize for trade
capital = max_risk - reduction*int(risk_level) 
capital = capital / len(prices) # how much when inc average down
print("Buy the following amount of shares for each trade: risking "+str(capital)+" per trade")
for x in prices:
    print(str(int(capital)/float(x))+" of shares at price $" + str(x))
