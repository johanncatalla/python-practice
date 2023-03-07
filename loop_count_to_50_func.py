def count50(i):
    if i <= 50:
        input = [x for x in range(1,i+1)]
        sliced = [input[i:i+10] for i in range(0, len(input), 10)]
        for i in sliced:
            for j in i:
                print(j, end=' ') 
            print()
def main():
    num = int(input('Enter number: '))
    count50(num)

main()
