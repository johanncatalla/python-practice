'''
Write a program that receives a temperature in Celsius as input and display a message depending on the temperature state.



a.) Below 0 degrees, print "Freezing cold!"
b.) 0-10 degrees, print "Very cold!"
c.) 11-20, print "Cold!"
d.) 20-30, print "Quite Normal!"
e.) 31-40, print "It's getting hot!"
f.) 41 above, print "It's very hot!"

'''

temp = float(input("Enter temperature: "))

if temp <= 0:
    print('Freezing cold!')
else:
    if temp <= 10 > 0:
        print('Very cold!')
    else:
        if temp == 20:
            print('Quite Normal!')
        if temp <= 20 >= 11:
            print('Cold!')
        else:
            if temp <= 30 >= 20:
                print('Quite Normal!')
            else:
                if temp <= 40 >= 31:
                    print('It\'s getting hot!')
                else:
                    if temp >= 41: 
                        print('It\'s very hot!')
                         
