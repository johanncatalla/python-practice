def skyscraper(w,h):
    top = ["*","**"]
    space = " "
    if w % 2 == 0:
        print(space * (w//2),"**",sep='', end='')
    else:
        print(space * ((w//2)+1),"*", sep='', end='')
    print()
    for x in range(1,h-1):
        print(space, '*' * (w), sep='', end='\n')
    print('*' * (w+2), sep='', end='')

def main():
    w,h = int(input('Enter width: ')), int(input('Enter height: '))
    skyscraper(w,h)

main()