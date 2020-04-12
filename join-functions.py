import json

import json

with open('C:\\Users\\slugg\\Documents\\GitHub\\Hash-Join\\Hash-Join\\data1.json') as a:
    data1 = json.load(a)

with open('C:\\Users\\slugg\\Documents\\GitHub\\Hash-Join\\Hash-Join\\data2.json') as b: 
    data2 = json.load(b)

# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
print(data1)
print((type(data1)))
print(data2)

hashTable = [[] for _ in range(10)]
print(hashTable)

def hashVal(key):
    return key % len(hashTable)

print(hashVal(5))
print(hashVal(9))

def insert(hashTable, key, value):
    intKey = int(key)
    hashKey = hashVal(intKey)
    hashTable[hashKey].append(value)

#insert(hashTable, 5, 'Nepal')
#insert(hashTable, 5, 'Naples')

for key, value in data1.items():
    insert(hashTable, key, value)

for key, value in data2.items():
    insert(hashTable, key, value)

print(hashTable)

