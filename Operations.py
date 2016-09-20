'''
Created on May 24, 2015

@author: mewolot
'''
from base64 import standard_b64encode
from base64 import standard_b64decode

def hex2Bin(hex):
    HexPairs = [(hex[i + 0], hex[i + 1]) for i in range(0,len(hex),2)]
    hexStr = ""
    for pair in HexPairs:
        hexStr += hex2Binary("" + pair[0] + "" + pair[1])
    charList = [chr(int(hexStr[i:i+8],2)) for i in range(0,len(hexStr),8)]
    hexChars = ""
    for item in charList:
        hexChars += "" + item
    return hexChars 

def hex2Binary(hexString):
    hexInt = int(hexString,16)
    #Fill 8 bytes
    binary = bin(hexInt)[2:].zfill(8)
    return binary

def Binary2Hex(binaryStr):
    left = int(binaryStr[0:4],2)
    right = int(binaryStr[4:],2)
    if left < 10:
        leftInt = "%d" % left
    else:
        if left == 10:
            leftInt = 'a'
        elif left == 11:
            leftInt = 'b'
        elif left == 12:
            leftInt = 'c'
        elif left == 13:
            leftInt = 'd'
        elif left == 14:
            leftInt = 'e'
        elif left == 15:
            leftInt = 'f'
        else:
            leftInt = 'X'
    if right < 10:
        rightInt = "%d" % right
    else:
        if right == 10:
            rightInt = 'a'
        elif right == 11:
            rightInt = 'b'
        elif right == 12:
            rightInt = 'c'
        elif right == 13:
            rightInt = 'd'
        elif right == 14:
            rightInt = 'e'
        elif right == 15:
            rightInt = 'f'
        else:
            rightInt = 'X'
    
    return leftInt + rightInt

def binary2Base64(binary):
    base64 = standard_b64encode(binary)
    return base64

def base642Binary(base64):
    binary = standard_b64decode(base64)
    return binary

def base642Hex(base64):
    binary = standard_b64decode(base64)
    hex = Binary2Hex(binary)
    return hex

def hex2Base64(hexString):
    binary = hex2Bin(hexString)
    base64 = binary2Base64(binary)
    return base64

# def XOR(Hex1, Hex2):
#     if len(Hex1) == 0:
#         return Hex2
#     elif len(Hex2) == 0:
#         return Hex1
#     difference = len(Hex1) - len(Hex2)
#     if difference > 0:
#         Hex2 = "0" * difference + Hex2
#     else:
#         Hex1 = "0" * difference + Hex1
#     HexPairs1 = [(Hex1[i + 0], Hex1[i + 1]) for i in range(0,len(Hex1),2)]
#     hexStr1 = ""
#     for pair in HexPairs1:
#         hexStr1 += hex2Binary("" + pair[0] + "" + pair[1])
#     HexPairs2 = [(Hex2[i + 0], Hex2[i + 1]) for i in range(0,len(Hex2),2)]
#     hexStr2 = ""
#     for pair in HexPairs2:
#         hexStr2 += hex2Binary("" + pair[0] + "" + pair[1])
#     xorStr = ""
#     for i in range(len(hexStr1)):
#         if int(hexStr1[i]) - int(hexStr2[i]) == 0:
#             xorStr += "0"
#         else:
#             xorStr += "1"
#     hexFinal = ""
#     for i in range(0,len(xorStr),8):
#         hexFinal += Binary2Hex(xorStr[i:i+8])
#     return hexFinal

def XOR(Hex1, Hex2):
    dec1 = int(Hex1,16)
    dec2 = int(Hex2,16)
    XORed = dec1 ^ dec2
    return (hex(XORed)).strip("0x L")
def str2Hex(str):
    hexStr = ""
    for letter in str:
        if letter == " ":
            hexStr += "20"
        else:
            hexadd = hex(ord(letter)).strip("0x")
            if len(hexadd) == 1:
                hexadd = "0" + hexadd
            hexStr += hexadd
    return hexStr

def rKeyXOR(message, key):
    messageHex = str2Hex(message)
    keyHex = str2Hex(key)
    endHex = ""
    for i in range(0,len(message)):
        endHex += XOR(str2Hex(message[i]),str2Hex(key[(i % len(key))]))    
    return endHex

def hamdist(str1, str2):
    hex1 = str2Hex(str1)
    hex2 = str2Hex(str2)
    dec1 = int("%s" % hex1, 16)
    dec2 = int("%s" % hex2, 16)
    binary1 = bin(dec1)
    binary2 = bin(dec2)
    dist = 0
    for bit1,bit2 in zip(binary1,binary2):
        if bit1 != bit2:
            dist += 1
    return dist

def binhamdist(binary1, binary2):
    dist = 0
    for bit1,bit2 in zip(binary1,binary2):
        if bit1 != bit2:
            dist += 1
    return dist
 
def indexOfMinimum(TupleList):
    min, mindex = TupleList[0]
    for item, index in TupleList:
        if item < min:
            min = item
            mindex = index
    return min, mindex
        

#print hamdist("this is a test", "wokka wokka!!!")


#print rKeyXOR("Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal","ICE")

# hex1 = raw_input("Enter Hex:\n")
# hex2 = raw_input("Enter Hex:\n")
# xor = XOR(hex1,hex2)
# print xor
