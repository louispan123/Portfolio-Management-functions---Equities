# There are the plotting modules and libraries we'll use:
#TO ADD: 
'''
- Figure out how to connect the dots with a line graph overlay. 
'''

import matplotlib as mpl
import matplotlib.pyplot as plt

# Command so that plots appear in the iPython Notebook
%matplotlib inline

# Average down, main function.     
def averagedown(quantity):
    entry = input("Put in the entry you currently have: ")
    current = input("Enter the current price: ")
    target = input("Enter the target price you want to average down to: ")
    buyquantity = buyquantit(quantity, entry, target, current)
    print("No. Shares you need to buy to average down is " + str(buyquantity))
    print('Other possible average down targets and corresponding quantity required are plotted below:')
    plottingad(quantity,entry,current)
    choice = input("Would you like to try another?")
    if "yes" in choice:
        quantity = input("Please enter new quantity or old one if no change: ")
        averagedown(quantity)

# Break even, main function. 
def breakeven(quantity):
    entry = input("Put in the entry you have: ")
    sl = input("Enter desired stop loss: ")
    reduceq = input("Enter no of shares you want to reduce your position by to breakeven: ")
    reducep = int(reduceq)/int(quantity)
    freetrade = freetrad(entry, sl, reducep)
    print("Percentage quantity reduction is " + str(reducep*100) + "%" + " and free trade target is " + str(freetrade) + "\n")
    print("Other possible scenarios with different quantity reductions and corresponding free trade targets are plotted below:")
    plottingbe(quantity,entry,sl)
    choice = input("Would you like to try another?")
    if "yes" in choice:
        quantity = input("Please enter new quantity or old one if no change: ")
        breakeven(quantity)        
        
# For plotting break even with different quantity reductions all the way to 0
def plottingbe(quantity, entry, sl):
    qreductions = [x for x in range(1,int(quantity)-1)]
    freetrades = [freetrad(entry, sl, x) for x in qreductions]
    plt.plot(qreductions,freetrades,'go')
    plt.xlabel('Shares Reduced')
    plt.ylabel('Target Required')

# For plotting different target average down prices with corresponding quantity required 
def plottingad(quantity, entry, current):
    targets = [x for x in range(int(current)+2,int(entry))]
    buyquantities = [buyquantit(quantity, entry, x, current) for x in targets]
    plt.plot(targets,buyquantities,'go')
    plt.xlabel('Target Price Average')
    plt.ylabel('Quantity Required')
    
# Identifies quantity required for purchase -- average down
def buyquantit(quantity, entry, target, current):
    return float(quantity)*(float(entry)-float(target))/(float(target)-float(current))

# Identifies requirement for a free trade -- free trade
def freetrad(entry, sl, reducep):
    return (float(entry)-float(sl))/float(reducep)+float(sl)

quantity = input("Enter current quantity of shares: ")
decision = input("Would you like to averagedown or breakeven? ")
if 'aver' in decision:
    averagedown(quantity)   
else:
    breakeven(quantity)
    
