
def findMedian(arr):
    arr.sort()
    #print(arr)
    #print(arr[len(arr)//2])
    return arr[len(arr)//2]

print(findMedian([0, 1, 2, 4, 6, 5, 3]))
print(findMedian([5, 3, 1, 2, 4]))