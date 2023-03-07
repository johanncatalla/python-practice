amount = float(input('Enter the amount: '))

#create denom list
bills = [1000, 500, 200, 100, 50, 20]
coins = [10, 5, 1,]
cents = [0.25, 0.01]

for x in bills: #x is every value in list
    count = amount // x #returns the floor value 
    amount = amount % x #returns the next amount to be floor divided
    print(f'P{x} bills: {count:.0f}') #prints floor value
    
    #loops until list runs out    
    
for x in coins:
    count = amount // x
    amount = amount % x
    print(f'P{x} coins: {count:.0f}')

for x in cents:
    count = amount / x #use normal division for cents
    amount = amount % x
    print(f'P{x * 100:.0f} cents: {count:.0f}')