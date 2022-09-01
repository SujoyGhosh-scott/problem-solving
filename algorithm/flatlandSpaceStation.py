def flatlandSpaceStations(n, c):
    c.sort()
    distances = [c[0] - 0, (n-1) - c[len(c) - 1]]
    for i in range(len(c) - 1):
        distances.append((c[i + 1] - c[i]) // 2)

    return max(distances)


nm = input().split()

n = int(nm[0])

m = int(nm[1])

c = list(map(int, input().rstrip().split()))

result = flatlandSpaceStations(n, c)

print("result")
print(result)