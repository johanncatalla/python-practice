'''
num = int(input('Enter n: '))
num = str(num)
lst = []
for x in num:
    if x in ('4,5,6,7,8,9'):
        lst.append(x)
        print(x)
    if x in ('0,1,2,3'):
        continue
if len(lst) == 0:
    print('none')
'''

num = input('Enter n: ')
 
none = True
for i in num:
    if int(i) > 3:
        print(i)
        none = False
if none:
    print("none")