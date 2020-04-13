import json

with open('C:\\Users\\slugg\\Documents\\GitHub\\Hash-Join\\Hash-Join\\data1.json') as a:
    data1 = json.load(a)
with open('C:\\Users\\slugg\\Documents\\GitHub\\Hash-Join\\Hash-Join\\data2.json') as b: 
    data2 = json.load(b)

totalBuckets = 10

#print(data1)
#print(data2)

hashTable1 = [[] for _ in range(totalBuckets)]
hashTable2 = [[] for _ in range(totalBuckets)]
FinalTable = [[] for _ in range(totalBuckets)]

def hashVal(key):
    return key % totalBuckets

def insert(hashTable, key, value):
    intKey = int(key)
    hashKey = hashVal(intKey)
    hashTable[hashKey].append(key)
    hashTable[hashKey].append(value)

for key, value in data1.items():
    insert(hashTable1, key, value)

for key, value in data2.items():
    insert(hashTable2, key, value)

print("This is the result of Hashing Table 1")
#print(hashTable1)
i = 0
for s in hashTable1:
    print("Bucket " + str(i))
    print(*s)
    i+=1
print("\nThis is the result of Hashing Table 2")
#print(hashTable2)
i = 0
for s in hashTable2:
    print("Bucket " + str(i))
    print(*s)
    i+=1

def merge(lst1, lst2):
    return [a + b for a, b in zip(lst1, lst2)] 

FinalTable = merge(hashTable1, hashTable2)
print("\nThis is the result of merging table 1 and 2")
#print(FinalTable)
i = 0
for s in FinalTable:
    print("Bucket " + str(i))
    print(*s)
    i+=1


def altElement(a):
    even = 0
    for i in range(len(a)):
        for j in range(len(a[i])):
            if even % 2 == 0:
                print(a[i][j])
            even+=1


print(altElement(FinalTable))