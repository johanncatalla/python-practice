num = int(input("Enter number: "))
g = 0
if num <= 50:
    for x in range(0, num):
        for y in range(10):
            if g == num:
                break
            print(g, end=' ')
            g += 1
        print()
        if g == num:
            break
else: 
    print('Number is higher than 50')
    