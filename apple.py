'''
JOHANN SEBASTIAN CATALLA
M002 
Homework
'''

apple = int(input("how many apples are bought? "))

floor_apl = apple // 12
mod_apl = apple % 12

initial_pay = floor_apl * 100
remainder = mod_apl * 10

print(f'''That is {floor_apl} dozens and {mod_apl} pieces
The total amount is {initial_pay + remainder}''')