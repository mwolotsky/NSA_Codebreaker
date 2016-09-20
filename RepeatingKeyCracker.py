'''
Created on Jun 9, 2015

@author: mewolot
'''
import Operations as op
import base64
import numpy
import Single_Byte as sb
from __builtin__ import str

def findKeySize(hexStr):
    dec = int(hexStr,16)
    binaryStr = bin(dec)
    Distances = []
    for keySize in range(2,40):
        firstPart = binaryStr[0:keySize * 8]
        secondPart = binaryStr[keySize * 8: keySize * 8 * 2]
        Distances.append(((op.binhamdist(firstPart, secondPart) / 1.0 / keySize),keySize))
           
    min = 2
    val = Distances[0][0]
    for num, key in Distances:
        if num < val:
            val = num
            min = key
#     print numpy.array(Distances)
#     exit()
    return min





file = open("key_hex_enc","r")
#base64Str = ""
#for line in file:
#    base64Str += line
hexStr = file.read()
file.close()
#b64 = base64.standard_b64decode(base64Str)
#hexStr = op.str2Hex(b64)

keySize = findKeySize(hexStr)
# keySize = 5

splitBlocks = [hexStr[i:i + keySize * 2] for i in range(0,len(hexStr),keySize * 2)]

print hexStr
print splitBlocks


singleByteBlocks = []

for i in range(0,keySize):
    Block = []
    for b in splitBlocks:
        Block.append(b[i:i + 2])
    singleByteBlocks.append(Block)

print singleByteBlocks

Cracked = []
for b in singleByteBlocks:
    str = ""
    for item in b:
        str += item
    list = sb.bestScoring(str)
#     print list
    betterList = []
    for item in list[0]:
        if "\\" not in item:
            betterList.append(item)
    for line in betterList:
        print line
    print

    Cracked.append(betterList)
    
print

reconstructed = []

 
