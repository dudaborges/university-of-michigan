animal = dict()
animal['dog'] = 'Jully'
animal['cat'] = 'bibi'
print(animal)

for key in animal:
    print(animal[key])

listAnimal = []
for key in animal:
    listAnimal.append(key)
print(listAnimal)