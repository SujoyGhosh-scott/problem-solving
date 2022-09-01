def weightedUniformStrings(s, queries):
    return None

s = input()
queries_count = int(input().strip())
queries = []
for _ in range(queries_count):
    queries_item = int(input().strip())
    queries.append(queries_item)
result = weightedUniformStrings(s, queries)