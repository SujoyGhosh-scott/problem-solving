n = int(input())
pairs = []
for i in range(1, n+1):
    for j in range(1, n+1):
        if i*j == 12:
            x = [i, j]
            x.sort()
            if x not in pairs:
                pairs.append(x)

#print(pairs)
print(len(pairs))
