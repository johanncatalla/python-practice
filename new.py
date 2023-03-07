def display():
    print("Thank you for using this app! Join my patreon :)")

x = 1 
y = 9
k = (x+y)
string = (x*y+k)
print(string)

validity = k
if k <=5:
    validity="insignificant"
else:
    validity="significant"
    

msg= f'The value of x is {x} while y is {y}, therefore the value of k is {k} which is {validity}'


print(msg)

display () 