import json

with open('C:\\Users\\slugg\\Documents\\GitHub\\Hash-Join\\Hash-Join\\data1.json') as a:
    data1 = json.loads(a.read())
with open('C:\\Users\\slugg\\Documents\\GitHub\\Hash-Join\\Hash-Join\\data2.json') as b: 
    data2 = json.load(b)

totalBuckets = 10

hashTable1 = [[] for _ in range(totalBuckets)]
hashTable2 = [[] for _ in range(totalBuckets)]
FinalTable = [[] for _ in range(totalBuckets)]

def hashVal(key):
    return key % totalBuckets

def insert(hashTable, key, obj):
    intKey = int(key)
    hashKey = hashVal(intKey)
    hashTable[hashKey].append(obj)

def compare(hashTable):
    for i in range(len(hashTable)):
        for key in range(len(hashTable[i])):
            checkTable2(i, key, hashTable[i][key]['ID'],hashTable[i][key])

def checkTable2(i, key, id, dictVal):
    checked = False
    for j in range(len(hashTable2[i])):
        if(hashTable2[i][j]['ID'] == id):
            if (checked == False):
                newDict = {}
                newDict.update(dictVal)
                newDict.update(hashTable2[i][j])
                FinalTable[i].append(newDict)
                checked = True
            else:
                FinalTable[i][key].update(hashTable2[i][j])

for j in data1:
    insert(hashTable1, j['ID'], j)

for j in data2:
    insert(hashTable2, j['ID'], j)

compare(hashTable1)
print("\n\n")

print("Hashed R1")
for s in hashTable1:
    print(*s)

print("\nHashed R2")
for s in hashTable2:
    print(*s)

print("\nFinal Hash Join")
for s in FinalTable:
    print(*s)
