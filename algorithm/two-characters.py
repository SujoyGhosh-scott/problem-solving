def alternate(s):
    substrings = []
    occurances = []
    for i in range(len(s) - 1):
        x = s[i] + s[i+1]
        if x in substrings:
            continue
        substrings.append(x)
        occurances.append(s.count(x))
    print(substrings)
    print(occurances)
    #first letter of the max substring
    maxSubstring = substrings[occurances.index(max(occurances))]
    a = maxSubstring[0]
    return s.count(a)

l = int(input().strip())
s = input()
result = alternate(s)

print(result)