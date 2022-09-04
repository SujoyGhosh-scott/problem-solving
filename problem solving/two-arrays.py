def twoArrays(k, A, B):
    sum = 0
    for i in A:
        sum += i
    for i in B:
        sum += i
    avg = sum // len(A)
    if avg >= k:
        return 'YES'
    else:
        return 'NO'