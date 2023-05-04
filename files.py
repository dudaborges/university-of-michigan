file = open('test.txt')
readFile = file.read().split()
email = readFile[0]
print(email.split('@'))
print(readFile)
print(len(readFile))
for line in readFile:
    if line.startswith('from'):
        print('from', line)

