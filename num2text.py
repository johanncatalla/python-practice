#list method

list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

num = int(input('Enter number: '))

if num < 10:
    print(list[num])
elif num < 20:
    print(teens[num - 10])
elif num % 10 == 0:
    num = int(num)
    print(tens[num // 10 - 2])
else:
    if num % 10 != 0:
        print(f'{tens[num // 10 - 2]}-{list[num % 10]}')
        
'''
#dictionary method

ones = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
tens1 = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
tens2 = {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}

num = int(input("Enter the number to be translated: "))

if num < 10:
    print(ones[num])
elif num <= 19 >= 10:
    print(tens1[num])
elif num % 10 == 0: 
    if num <= 90 >= 20:
        print(tens2[num / 10]) 
elif num % 10 != 0:  
    if num <= 99 > 20:
       print(f'{tens2[num // 10]}-{ones[num % 10]}')
'''