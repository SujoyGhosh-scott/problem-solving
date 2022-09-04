def countingSort(arr):
    ans = [0]*100
    res = ""
    for i in arr:
        ans[i] = ans[i] + 1
    
    for i in range(0, 100):
        if ans[i] != 0:
            for j in range(0, ans[i]):
                #print(i, end=" ")
                res = res + str(i) + " "
    print(res[:-1])