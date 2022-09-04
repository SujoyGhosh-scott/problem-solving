
def maximizingXor(l, r):
    max = 0
    for i in range(l, r+1):
        for j in range(l, r+1):
            if i ^ j > max :
                max = i ^ j
    return max


print(maximizingXor(10, 15))
print(maximizingXor(11, 100))