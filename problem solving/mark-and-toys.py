def maximumToys(prices, k):
    prices.sort()
    comb = []
    for i in range(0, len(prices)):
        temp = []
        sum = 0
        for j in range(i, len(prices)):
            if(sum + prices[j] > k):
                break
            else:
                sum += prices[j]
                temp.append(prices[j])
        if(len(temp) > 0):
            comb.append(temp)
    max = 0
    for i in comb:
        if(len(i) > max):
            max = len(i)
    return max


print(maximumToys([1,2,3,4], 7))
print(maximumToys([1, 12, 5, 111, 200, 1000, 10], 50))