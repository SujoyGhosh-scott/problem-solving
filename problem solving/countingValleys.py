#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    seaLevel = 0 
    currentLevel = 0 
    mountainCount = 0 
    vallyCount = 0 
    isVally = False 
    atSeaLevel = True
    for i in path:
        if(atSeaLevel):
            if(i == 'U'):
                isVally = False
            else: 
                isVally = True
        if(i == 'U'):
            currentLevel += 1
        else:
            currentLevel -= 1
        if(currentLevel == 0):
            atSeaLevel = True
        else:
            atSeaLevel = False
        if(atSeaLevel and isVally):
            vallyCount += 1
        elif(atSeaLevel and not isVally):
            mountainCount += 1
    return vallyCount
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
