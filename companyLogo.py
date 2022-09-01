def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j][0] > arr[j + 1][0] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


s = input()
distinctElements = list(set(s))

letterCounter = []
letterCounts = []

for i in distinctElements:
    counter = 0
    for j in s:
        if(j == i):
            counter = counter + 1

    letterCounter.append([i, counter])
    letterCounts.append(counter)

#sorting the final lettercounter
bubbleSort(letterCounter)

'''
print("letter counter")
print(letterCounter)
print("letter counts")
print(letterCounts)
'''
finalList = []

for i in range(3):
    for j in range(len(letterCounter)):
        if(letterCounter[j][1] == max(letterCounts)):
            finalList.append(letterCounter[j])
            #remove the max element from letter counts
            letterCounts.remove(max(letterCounts))
            del letterCounter[j]
            break
'''
print("final list")
print(finalList)
'''

for i in range(3):
    print(finalList[i][0], finalList[i][1])
