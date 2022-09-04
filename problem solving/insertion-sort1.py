def insertionSort1(n, arr):
    key = arr[n-1]
    i = n-1
    while i-1 >= 0 and  key < arr[i-1]:
        arr[i] = arr[i-1]
        [print(j, end = " ") for j in arr]
        i -= 1
        print()
    arr[i] = key
    [print(j, end=" ") for j in arr]


insertionSort1(5, [1,2,4,5,3])
insertionSort1(5, [2,4,6,8,3])

