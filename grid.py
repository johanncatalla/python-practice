def gridSum(grid):
    sum = 0
    curr = 0
    
    for lst in grid:
        sum += lst[curr]
        curr += 1
    return sum

grid = [[1,2,3],[1,2,3],[1,2,3]]
res = gridSum(grid)
print(res)