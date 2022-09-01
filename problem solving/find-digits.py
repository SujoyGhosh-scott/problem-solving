def findDigits(n):
    strNum = str(n)
    ans = 0
    for i in strNum:
        if(int(i) == 0):
            continue
        if(n%int(i) == 0):
            ans+=1
    return ans


print(findDigits(12))
print(findDigits(1012))