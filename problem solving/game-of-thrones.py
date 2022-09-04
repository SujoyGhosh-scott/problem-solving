def gameOfThrones(s):
    if len(s) <= 1:
        return 'NO'
    evenLength = len(s) % 2 == 0
    letters = set(s)
    multipleSingleLetters = False
    #print(letters)
    for i in letters:
        if s.count(i) == 1:
            if not evenLength:
                if not multipleSingleLetters:
                    multipleSingleLetters = True
                else:
                    return 'NO'   

    return 'YES'

print(gameOfThrones('a'))
print(gameOfThrones('aaabbbb'))
print(gameOfThrones('cdefghmnopqrstuvw'))
print(gameOfThrones('cdcdcdcdeeeef'))