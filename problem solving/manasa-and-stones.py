def stones(n, a, b):
    inps = [a,b]
    ans = []
    for i in range(0, n):
        sum = 0
        for j in range(0, i):
            sum += inps[0]
        for k in range(i, n-1):
            sum += inps[1]
        ans.append(sum)
    
    #print(ans)
    unique_set = set(ans)
    unique_vals = (list(unique_set))
    unique_vals.sort()

    return unique_vals


print(stones(3,1,2))
print(stones(4,10,100))
print(stones(18,28,28))


