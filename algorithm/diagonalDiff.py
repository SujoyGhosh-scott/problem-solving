def diagonalDifference(arr):
    dig1 = 0
    dig2 = 0
    for i in range(len(arr)):
        dig1 = dig1 + arr[i][i]
        dig2 = dig2 + arr[len(arr)-i-1][i]

    return abs(dig1 - dig2)

n = int(input().strip())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))
result = diagonalDifference(arr)
print(result)