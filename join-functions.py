import json

with open('C:\\Users\\slugg\\Documents\\GitHub\\Hash-Join\\Hash-Join\\data1.json') as a:
    data1 = json.load(a)
with open('C:\\Users\\slugg\\Documents\\GitHub\\Hash-Join\\Hash-Join\\data2.json') as b: 
    data2 = json.load(b)

totalBuckets = 10

hashTable1 = [[] for _ in range(totalBuckets)]
hashTable2 = [[] for _ in range(totalBuckets)]
FinalTable = [[] for _ in range(totalBuckets)]

def hashVal(key):
    return key % totalBuckets

def insert(hashTable, key, value):
    intKey = int(key)
    hashKey = hashVal(intKey)
    hashTable[hashKey].append(value)

for key, value in data1.items():
    insert(hashTable1, key, value)

for key, value in data2.items():
    insert(hashTable2, key, value)

print("This is the result of Hashing Table 1")
print(hashTable1)
print("\nThis is the result of Hashing Table 2")
print(hashTable2)

def merge(lst1, lst2):
    return [a + b for a, b in zip(lst1, lst2)] 

FinalTable = merge(hashTable1, hashTable2)
print("\nThis is the result of merging table 1 and 2")
print(FinalTable)