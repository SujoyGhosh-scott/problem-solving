def allBugsHappy(b):
    if b[0] != b[1]:
        return False
    if b[len(b)-1] != b[len(b)-2]:
        return False
    for i in range(1, len(b)-1):
        if b[i] != b[i-1] and b[i] != b[i+1]:
            return False
    return True


def happyLadybugs(b):
    #if string contains only _ return YES
    if(b.count('_') == len(b)):
        return 'YES'

    #if any of the letter count is 1, return NO
    for i in b:
        if i == '_':
            continue
        if b.count(i) == 1 :
            return 'NO'

    #if all the ladybugs are already happy in the given string, return YES
    #if not, check if there is room for swapping letters
    ##if there are _, return YES
    ##else return NO
    if allBugsHappy(b) == True:
        return 'YES'
    else:
        if b.count('_') > 0:
            return 'YES'
        else:
            return 'NO'

# print(happyLadybugs('RBY_YBR'))      #yes
# print(happyLadybugs('X_Y__X'))       #no
# print(happyLadybugs('__'))           #yes
# print(happyLadybugs('B_RRBR'))       #yes
# print(happyLadybugs('AABBC'))        #no
# print(happyLadybugs('AABBC_C'))      #yes
# print(happyLadybugs('_'))            #yes
# print(happyLadybugs('DD__FQ_QQF'))   #yes
# print(happyLadybugs('AABCBC'))       #no
print(happyLadybugs('_'))
print(happyLadybugs('RBRB'))
print(happyLadybugs('RRRR'))
print(happyLadybugs('BBB'))
print(happyLadybugs('BBB_'))
