list = [1,2,3,4,5,-9]
combinations = [(a,b) for idx, a in enumerate(list) for b in list[idx+1:]]
sums = [abs(sum(i)) for i in combinations]
dict = dict(zip(combinations, sums))
print(*min(dict, key=dict.get), sep=" + ", end=" = ")
print(min(sums))
