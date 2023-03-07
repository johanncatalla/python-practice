width = int(input('Enter width: '))
height = int(input('Enter height: '))

space = (' ')
fig = "*"
for tower in range(1, height + 1):
    for top in range(0, width - (width - 1)):
        if width % 2 != 0: 
            print(space * (width // 2 + 1), end="")
            print(fig, end=" ")
        if width % 2 == 0:
            print(space * (width // 2), end="")
            print('**', end=" ")
        print()
    for body in range(1, height - 1):
        print(space, end='')
        for x in range(width):
            print(fig, end='')
        print()
    if height > 1:
        for base in range(height):
            for x in range(width+2):
                print('*', end='')
            print()
            break   
    break
    
'''
width = int(input('Enter the width of skyscraper: '))
height = int(input('Enter height of skyscraper: '))
space1 = (' ')
k = 0
for top in range(0, width - (width-1)):
    for space in range(1):
        space1 = space1 * (width//2)
    if width % 2 == 0:
        print(space1, end='')
        print('**')
    if width % 2 != 0:
        space1 += (' ')
        print(space1, end='')
        print('*')
for i in range(2, height):
    for space in range(1):
        print(end=" ")
    if k == height:
        break
    for k in range(1, width+1):
        print("*", end="")
        k += 1
    k = 0
    print()
for base in range(width + 1):
    star = '*' * width
    print(star, end='')
'''
