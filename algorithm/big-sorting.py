def bigSorting(unsorted):
    unsorted.sorted()
    for i in unsorted:
        print(i)

n = int(input().strip())
unsorted = []
for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)
result = bigSorting(unsorted)