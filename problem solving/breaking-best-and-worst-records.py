def breakingRecords(scores):
    most = 0
    least = 0
    currMost = scores[0]
    currLeast = scores[0]
    for i in scores:
        if i > currMost:
            most+=1
            currMost = i
        elif i < currLeast:
            least += 1
            currLeast = i

    return [most, least]

print(breakingRecords([10,5,20,20,4,5, 2, 25, 1]))
print(breakingRecords([3, 4, 21, 36, 10, 28, 35, 5, 24, 42]))