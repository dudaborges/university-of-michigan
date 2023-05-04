listName = ['maria', 'joao', 'maria', 'felipe', 'joao', 'joao']
counts = dict()
count = 0
for name in listName:
    counts[name] = counts.get(name, 0) + 1
print(counts)
