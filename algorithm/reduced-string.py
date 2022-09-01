def superReducedString(s):
    if s == '':
        return "Empty String"
    changed = False
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            oldVal = s[i] + s[i]
            s = s.replace(oldVal, '')
            changed = True
            break
    #print(s)
    if changed:
        s = superReducedString(s)
    return s

s = input()
result = superReducedString(s)
print(result)