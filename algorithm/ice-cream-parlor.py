def icecreamParlor(m, arr):
    #setting up initial result
    res = [0, 1]
    #flag to get out of the loop asa we get right answer
    found = False
    for i in range(len(arr)):
        for j in range(len(arr)):
            #no need to check for same index
            if i == j:
                continue
            
            if arr[i] + arr[j] == m:
                found = True
                res[0] = i
                res[1] = j
                break
            else:
                prevDiff = m - (arr[res[0]] + arr[res[1]])
                currDiff = m - (arr[i] + arr[j])
                if(prevDiff > currDiff and currDiff > 0):
                    res[0] = i
                    res[1] = j
        if found == True:
            break 
    res.sort()
    res[0] = res[0] + 1
    res[1] = res[1] + 1
    return res

t = int(input().strip())

for t_itr in range(t):
    m = int(input().strip())
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = icecreamParlor(m, arr)
    print(result)