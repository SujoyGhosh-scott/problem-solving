def missingNumbers(arr, brr):
    arr1 = set(arr)
    brr1 = set(brr)
    list = []
    ans = []
    if len(arr1) > len(brr1):
        list = arr
    else:
        list = brr
    for i in list:
        if(i in arr and i in brr and arr.count(i) == brr.count(i)):
            continue
        else:
            if i not in ans:
                ans.append(i)

    ans = set(ans)

    return sorted(ans)


print(missingNumbers([203, 204, 205, 206, 207, 208, 203, 204, 205, 206], 
[203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204]))
print(missingNumbers([7,2,5,3,5,3], [7,2,5,4,6,3,5,3]))