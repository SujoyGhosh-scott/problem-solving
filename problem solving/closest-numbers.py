def closestNumbers(arr):
    arr.sort()
    minDiff = 1000000
    for i in range(len(arr)-1):
        if(arr[i+1]-arr[i] <= minDiff):
            minDiff = arr[i+1]-arr[i]
    finalList = []
    for i in range(len(arr)-1):
        if(arr[i+1]-arr[i] == minDiff):
            finalList.append(arr[i])
            finalList.append(arr[i+1])
    return finalList


print(closestNumbers([5,4,3,2]))
print(closestNumbers([-20, -3916237, -357920, -3620601, 7374819, -7330761, 30, 6246457, -6461594, 266854, -520,-470]))
