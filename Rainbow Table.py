'''
Simple Rainbow Table Construction 
using, a dictionary
'''
import itertools
import hashlib

rainbowTable = {}

print("Create Simple Rainbow Table")
for variations in range(3,5):
    for pwTuple in itertools.product("xyz", repeat=variations):
        pw = ""
        md5Hash = hashlib.md5()
        for eachChr in pwTuple:
            pw = pw+"".join(eachChr)
        pw = bytes(pw, 'ascii')
        md5Hash.update(pw)
        md5Digest = md5Hash.hexdigest()
        rainbowTable[md5Digest] = pw

print("Rainbow Size: ", len(rainbowTable), "\n")
for hashValue, pwValue in rainbowTable.items():
    print(hashValue, pwValue)
    
            
            
