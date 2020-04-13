import json

with open('C:\\Users\\slugg\\Documents\\GitHub\\Hash-Join\\Hash-Join\\data1.json') as a:
    data1 = json.loads(a.read())
with open('C:\\Users\\slugg\\Documents\\GitHub\\Hash-Join\\Hash-Join\\data2.json') as b: 
    data2 = json.load(b)

#print(data1[1]['ID'])

totalBuckets = 3

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
            #print("Table 1 dict Value " + str(hashTable[i][key]))
            #print("TB 1 ID " + str(hashTable[i][key]['ID']))
            #print(hashTable[i][key]['name'])
            #checkTable2(i, key, hashTable[i][key]['ID'])
            print("\n")
            checkTable2(i, key, hashTable[i][key]['ID'],hashTable[i][key])




def checkTable2(i, key, id, dictVal):
    #print("Table 2 dict Value " + str(hashTable2[i][key]))
    print("Table 1 ID " + str(id))
    print("Table 2 ID " + str(hashTable2[i][key]['ID']))
    #print("Table 2 Grade " + str(hashTable2[i][key]['Grade']))
    checked = False
    for j in range(len(hashTable2[i])):
        print(j)
        print(hashTable2[i][j]['ID'])
        if(hashTable2[i][j]['ID'] == id):
            if (checked == False):
                newDict = {}
                newDict.update(dictVal)
                newDict.update(hashTable2[i][j])
                print("New Dict " + str(newDict))
                print(i)
                FinalTable[i].append(newDict)
                checked = True
            else:
                FinalTable[i][key].update(hashTable2[i][j])
                print("\nHIT ELSE\n")
            print(FinalTable)
            
        


for j in data1:
    #hashTable1[1].append(j)
    insert(hashTable1, j['ID'], j)

for j in data2:
    #hashTable1[1].append(j)
    insert(hashTable2, j['ID'], j)

#print("This is the result of Hashing Table 1")
#print(hashTable1)

#print("\nThis is the result of Hashing Table 2")
#print(hashTable2)
#print("\n")
#print(hashTable1[0][0]['ID'])
#print(hashTable1[0][0]['name'])
#print(hashTable2[0][1]['ID'])

compare(hashTable1)
print("\n\n")

for s in FinalTable:
    print(*s)
