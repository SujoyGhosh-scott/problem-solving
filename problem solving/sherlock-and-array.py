def balancedSums(arr):
    for i in range(0, len(arr)):
        if(sum(arr[:i]) == sum(arr[i+1:])):
            return 'YES'
    return 'NO'

print(balancedSums([1, 1, 4, 1,1]))
print(balancedSums([2, 0, 0, 0]))
print(balancedSums([0,0,2,0]))
print(balancedSums([1, 2, 3]))
print(balancedSums([1, 2, 3, 3]))