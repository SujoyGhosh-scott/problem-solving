def timeInWords(h, m):
    numberInWords = ["zero", "one", "two", "three", "four", "five", "six", 
    "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", 
    "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "twenty one",
    "twenty two", "twenty three", "twenty four", "twenty five", "twenty six", 
    "twenty seven", "twenty eight", "twenty nine"]

    if m == 0:
        return numberInWords[h] + " " + 'o\' clock'
    elif m == 1:
        return "one minute past " + numberInWords[h]
    elif m == 15:
        return "quarter past " + numberInWords[h]
    elif m == 30:
        return "half past " + numberInWords[h]
    elif m == 45:
        if h == 12:
            return "quarter to one"
        else:
            return "quarter to " + numberInWords[h + 1]
    elif m < 30:
        return numberInWords[m] + " minutes past " + numberInWords[h]
    else:
        if h == 12:
            return numberInWords[60 - m] + " minutes to one"
        else:
            return numberInWords[60 - m] + " minutes to " + numberInWords[h + 1]

    

h = int(input())
m = int(input())
result = timeInWords(h, m)
print(result)
