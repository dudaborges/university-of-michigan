objectList = ['computer', 'tv', 'computer', 'tv', 'tv', 'computer', 'computer']
count = dict()

for objects in objectList:
    count[objects] = count.get(objects, 0) + 1

for objects in count:
    print(count.values())

print(max(count.values()))
print(count)