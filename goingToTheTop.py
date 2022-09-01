def getRank(l, newRank):
    x = []
    x.extend(l)
    temp = -999
    for i in x:
        if i < newRank:
            temp = i
            break
    if temp == -999:
        x.append(newRank)
    else:
        x.insert(x.index(temp), newRank)
    #finalx = list(set(x))
    #print(x)
    #print(finalx)
    print(x.index(newRank) + 1)

n = int(input())
l1 = [int(i) for i in input().split()][:n]
m = int(input())
l2 = [int(i) for i in input().split()][:m]

for i in l2:
    getRank(l1, i)