'''
Created on Jun 1, 2015

@author: mewolot
'''
from Operations import XOR as xor
import FreqAnal
from matplotlib.cbook import Null

def singleXOR(fullHex, hex):
    bLength = len(fullHex) / 2
    byteFull = ("%s" % hex) * bLength
    answer = xor(fullHex,byteFull)
    return answer
    
def hex2Str(endHex):
    endList = [endHex[x:x+2] for x in range(0,len(endHex),2)]
    decList = [int(x,16) for x in endList]
    charList = [chr(x) for x in decList]
    str = ""
    for x in charList:
        str += "%s" % x
    return str

def dec2Hex(decimal):
    pair = [decimal / 16, decimal % 16]
    return "%s%s" % (pair[0],pair[1])

def bestScoring(fullHex):
    Dict = {}
    Numbers = []
    for i in range(0,256):
        endHex = singleXOR(fullHex,dec2Hex(i))
        plaintext = hex2Str(endHex)
        score = FreqAnal.englishFreqMatchScore(plaintext)
        Numbers.append(score)
        if score not in Dict.keys():
            Dict[score] = []
        Dict[score].append(plaintext)
        Numbers.append(score)
    Numbers = sorted(Numbers)
    
    return Dict[Numbers[len(Numbers)-1]], Numbers[len(Numbers)-1]
    

# fullHex = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
# print bestScoring(fullHex)




