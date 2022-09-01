#checkprime
def checkPrime(n):
    i=2
    while i<=n//2+1:
        if n % i == 0:
            return False
        i = i+1
    return True

#get all primes
def getPrimesInRange(n, m):
    i=n
    primes = []
    while i<=m:
        if checkPrime(i):
            primes.append(i)
        i = i+1
    #print("list of primes")
    #print(primes)
    pairs = []
    for i in range(len(primes)):
        for j in range(len(primes) - 1):
            if abs(primes[j] - primes[i]) == 2:
                x = [primes[j], primes[i]]
                x.sort()
                if x not in pairs:
                    pairs.append(x)

    #print("pairs")
    #print(pairs)
    print(len(pairs))



n, m = map(int,input().split())
getPrimesInRange(n, m)
#print(m)
#print(n)