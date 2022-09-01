def jimOrders(orders):
    preperationTime = []
    for i in orders:
        preperationTime.append(i[0] + i[1])
    for i in range(len(orders)):
        #print(preperationTime.index(min(preperationTime))+1, end=" ")
        if(i == len(orders)-1):
            print(preperationTime.index(min(preperationTime))+1)
        else:
            print(preperationTime.index(min(preperationTime))+1, end=" ")
        preperationTime[preperationTime.index(min(preperationTime))] = 10000


jimOrders([[1,3], [2,3], [3,3]])
print()
jimOrders([[8,1], [4,2], [5,6], [3,1], [4,3]])