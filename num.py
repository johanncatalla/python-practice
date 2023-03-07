a = input('Enter: ')

if a.isnumeric():
    if int(a) <= 5 >= 0:
        print('first-half')
    elif int(a) <= 9 >= 6: 
        print('Second-half')
 
if a.isalpha() and a.islower():
    if a in "aeiou":
        print('Small')
        print('Vowel')
    else:
        print('Snall')
        print('Consonant')

if a.isalpha() and a.isupper():
    if a in "AEIOU":
        print('Big')
        print('Vowel')
    else:
        print('Big')
        print('Consonant')