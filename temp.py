temperature = float(input("Enter temperature: "))

if temperature < 0:
    print('Freezing cold!')
    
else:
    if temperature == 10 >= 0:
        print('Very cold!')
    
    else:
        if temperature == 11 <= 20:
            print('Cold!')
    
        else:
            if temperature == 20 <= 30:
                print('Normal')
    
            else:
                if temperature == 31 <= 40:
                    print('It\'s getting hot!')
    
                else: 
                    if temperature >= 41:
                        print('It\'s very hot!')