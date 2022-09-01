def getRank(l, newRank):
    allranks = l
    i=0
    while allranks[i] >= newRank:
        i = i+1
    allranks.insert(newRank)
    allranks.reverse()
    ind = allranks.index(newRank)
    print(ind)

n = int(input().strip())

l1 = list(map(int,input().split()))

m = int(input())

l2 = list(map(int,input().split()))

for i in range(m):
    #print(l1, l2[i])
    getRank(l1, l2[i])

#print(l1)
#print(l2)