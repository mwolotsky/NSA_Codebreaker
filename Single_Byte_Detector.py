'''
Created on Jun 9, 2015

@author: mewolot
'''

import Single_Byte as sb
from _ast import Num

file = open("key_hex_enc","r")
Hex = [line.strip("\n") for line in file]
file.close()

best = 0
BestList = []
for item in Hex:
    try:
        List, num = sb.bestScoring(item)
    except:
        continue
    if num > best:
        best = num
        BestList = List
    elif num == best:
        BestList = BestList + List
    else:
        pass

print BestList
print best
