def pickingNumbers(a):
    sets = []
    for i in a:
        temp1 = i-1
        temp2 = i+1
        if temp1 in a:
            l1 = []
            for j in a:
                if j==i or j==temp1:
                    l1.append(j)
            sets.append(l1)
        elif temp2 in a:
            l2 = []
            for j in a:
                if j==i or j==temp2:
                    l2.append(j)
            sets.append(l2)

    print(sets)
    longest = 0
    for i in sets:
        if len(i) > longest:
            longest = len(i)
    return longest


pickingNumbers([4,6,5,3,3,1])

#pickingNumbers([1,2,2,3,1,2])

#pickingNumbers([4 97 5 97 97 4 97 4 97 97 97 97 4 4 5 5 97 5 97 99 4 97 5 97 97 97 5 5 97 4 5 97 97 5 97 4 97 5 4 4 97 5 5 5 4 97 97 4 97 5 4 4 97 97 97 5 5 97 4 97 97 5 4 97 97 4 97 97 97 5 4 4 97 4 4 97 5 97 97 97 97 4 97 5 97 5 4 97 4 5 97 97 5 97 5 97 5 97 97 97])

#pickingNumbers([66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66])

