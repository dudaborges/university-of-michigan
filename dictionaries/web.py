file = open('./dictionaries/web.txt', encoding="utf-8")
counts = dict()
for line in file:
    lineList = line.split()
    for words in lineList:
        word = words.lower()
        counts[word] = counts.get(word, 0) + 1
print(counts)

bigKey = None
bigValue = None

for key, value in counts.items():
    if bigValue is None or value > bigValue:
        bigValue = value
        bigKey = key

option = 0

def options(option):
    if option == 1:
        searchWord = str(input('Enter the word: ')).lower().strip()
        if searchWord in counts:
            print(f'Word "{searchWord}" found!')
        else:
            print(f'Word {searchWord} not found!')
    elif option == 2:
        print(f'The most repeated word is "{bigKey}", it repeated itself {bigValue} times')
    elif option != 1 and option != 2 and option != 3:
        print('[ERROR] Option not found.')

while option != 3:
    print('''
    [1] Search for word
    [2] Find most repeated word
    [3] Exit
    ''')
    try:
        option = int(input('Enter your option: '))
        options(option)
    except:
        print("[WARNING] Enter the numeric value.")


