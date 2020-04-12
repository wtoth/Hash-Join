import json

with open('C:\\Users\\slugg\\Documents\\GitHub\\Hash-Join\\Hash-Join\\data1.json') as a:
    data1 = json.load(a)
with open('C:\\Users\\slugg\\Documents\\GitHub\\Hash-Join\\Hash-Join\\data2.json') as b: 
    data2 = json.load(b)

totalBuckets = 9

hashTable = [[] for _ in range(totalBuckets)]

def hashVal(key):
    return key % len(hashTable)

print(hashVal(5))
print(hashVal(9))

def insert(hashTable, key, value):
    intKey = int(key)
    hashKey = hashVal(intKey)
    hashTable[hashKey].append(value)

for key, value in data1.items():
    insert(hashTable, key, value)

for key, value in data2.items():
    insert(hashTable, key, value)

print(hashTable)