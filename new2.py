def taxi():
    
    print('''
Welcome to my ride! :)
        ''')
    
    while True:
                 
        distance = float(input('Enter distance in km: '))
        rate = 5.00 
        totalfare = distance * rate
        
        if distance > 0:       
            print('''
            > That will be {}!
                '''.format(totalfare))
            break
            
        if distance <= 0:
            print('''
            > invalid distance
            ''')

    while True:
        
        amountpaid = float(input('Please enter payment in pesos: '))
        rate = 5.00 
        totalfare = distance * rate
        change = amountpaid - totalfare
        
        if amountpaid > totalfare:       
            print('''
            > You have paid {}, your change is {}
            '''.format(amountpaid, change))
            break
                 
        if amountpaid == totalfare:
            print('''
            > Exact amount received, thank you!
            ''')
            break     
       
        if amountpaid == 0:
            print('''
            > You have to pay :)
            ''')     
            
        if amountpaid < 0:
            print('''
            > I'm not paying you! :)
            ''')

        elif amountpaid != 0 != totalfare:
            z = totalfare - amountpaid
            print('''
            > Insufficient amount, you are {} pesos short. Please pay sufficient amount. Thank you!
            '''.format(z))
taxi()