def foundOddLetters(b):
    for i in b:
        if(i == '_'):
            continue
        if(b.count(i) % 2 == 1):
            return True
    return False


def solved(b):
    dashes = b.count('_')
    if dashes == len(b):
        return True
    for i in range(1,len(b)-1):
        if(b[i+1] != b[i] and b[i-1] != b[i]):
            return False
    print(b[-1])
    print(b[-2])
    if b[-1] != b[-2]:
        return False
    return True


def happyLadybugs(b):
    if(foundOddLetters(b)):
        return 'NO'
    if(solved(b)):
        return 'YES'
    else:
        if(b.count('_')>0):
            return 'YES'
        else:
            return 'NO'


# print(happyLadybugs('AABBC'))
# print(happyLadybugs('AABBC_C'))
# print(happyLadybugs('AABCBC'))
print(happyLadybugs('DD__FQ_QQF'))