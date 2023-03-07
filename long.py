amount = float(input('Enter the amount: '))

c = amount // 1000
d = amount % 1000
print(f'P1000 bills: {c:.0f}')
e = d // 500
f = d % 500
print(f'P500 bills: {e:.0f}')
g = f // 200 
h = f % 200 
print(f'P200 bills: {g:.0f}')
i = h // 100
j = h % 100 
print(f'P100 bills: {i:.0f}')
k = j // 50
l = j % 50
print(f'P50 bills: {k:.0f}')
m = l // 20
n = l % 20
print(f'P20 bills: {m:.0f}')
o = n // 10
p = n % 10
print(f'P10 coins: {o:.0f}')
q = p // 5 
r = p % 5
print(f'P5 coins: {q:.0f}')
s = r // 1
t = r % 1
print(f'P1 coins: {s:.0f}') 
u = t / 0.25 #Use regular division for cents
v = t % 0.25
print(f'P25 cents: {u:.0f}')
w = v / 0.01
x = v % 0.01
print(f'P1 cents: {w:.0f}')

        
    




