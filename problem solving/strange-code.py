def strangeCounter(t):
    # Write your code here
    max = 3
    loop = 3
    times = []
    for i in range(1, t+1):
        times.append(max)
        max-=1
        if max == 0:
            loop *= 2
            max = loop
    print(times)
    return times[t-1]


print(strangeCounter(1000000000000))
print(strangeCounter(21))
