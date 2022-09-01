def isKaprekarNumber(n):
    if(n==1):
        return True
    elif(n==2 or n==3 or n==4):
        return False

    square = pow(n,2)
    numlen = len(str(n))
    lhs = int(str(square)[:-numlen])
    rhs = int(str(square)[-numlen:])
    #print(rhs)
    #print(lhs)
    if(rhs+lhs == n):
        return True
    else:
        return False


def kaprekarNumbers(p, q):
    found = False
    for i in range(p,q+1):
        if(isKaprekarNumber(i)):
            print(i, end=" ")
            found = True
    print("INVALID RANGE")

kaprekarNumbers(1, 300)