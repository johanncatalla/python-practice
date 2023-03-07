def bills(amount: float) -> list:
    """Count number of bills

    Args:
        amount (float): Money to count per bills

    Returns:
        list: Number per bills
    """
    bills = [1000,500,200,100,50,20,10,5,1,0.25,0.01]
    lst = []
    for x in bills:
        if x == 0.01: 
            #regular division for one cent      
            res = amount / x
            amount = amount % x
            lst.append(f"P{x} = {res:.0f}") 
        else:
            #floor division for the rest
            res = amount // x
            amount = amount % x 
            lst.append(f"P{x} = {res:.0f}")
    return lst

def main():   
    amount = float(input('Enter amount: '))
    res = bills(amount)
    print(*res, sep='\n')

main()