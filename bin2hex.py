fStr = ""
file = open("key_enc",'r')
str = file.read()
for c in str:
    fStr += hex(ord(c))[2:]
file.close()
file = open("key_hex_enc",'w')
file.write(fStr)
file.close()
