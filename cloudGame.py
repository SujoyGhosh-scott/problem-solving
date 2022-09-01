n = int(input())
l = [int(i) for i in input().split()][:n]

i = 0
jumps = 0
while i < len(l):
    if i+2 >= len(l) or i+1 >= len(l):
        break
    if(l[i+2] == 1):
        i = i+1
    else:
        i = i+2
    jumps = jumps + 1

print(jumps)

#print(n)
#print(l)