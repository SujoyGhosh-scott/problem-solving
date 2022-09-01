import math

def encryption(s):
    sqr = math.sqrt(len(s))
    rows = math.floor(sqr)
    cols = math.ceil(sqr)

    matrix = []
    i = 0
    while True:
        if i >= len(s):
            break
        matrix.append(s[i: i + cols])
        i = i + cols
    print("matrix")
    print(matrix)

    encryptedText = ""
    for i in range(cols):
        x = ""
        for j in range(rows):
            if len(matrix[j]) - i == 1:
                continue
            x = x + matrix[j][i]
        #print(x)
        encryptedText = encryptedText + x + " "
    return encryptedText

s = input()
result = encryption(s)
print(result)