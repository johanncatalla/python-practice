memo = {}
def fib(num):
    if num <= 2:
        return 1
    if num in memo:
        return memo[num]
    memo[num] = fib(num - 1) + fib(num - 2)
    return memo[num]

res = fib(100)
print(res)