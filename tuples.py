d = {1: 'maria', 2: 'joao', 3: 'felipe'}
# classifca, ordena a lista tupla
# .items transforma o dicionário em dicionário com truplas
print(sorted(d.items()))
print(sorted(d.items(), reverse=True))
for k, v in d.items():
    print(k, v)
print(sorted([(v, k) for k,v in d.items()]))

l = list()
for k, v in d.items():
    # adicionar a lista em formato de tupla
    l.append((k, v))
