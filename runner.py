from pwn import *
import time

LIST = ["arm"]
for i in range(1000000):
    LIST.append("%d" % i)
f = open("INPUT",'w')
f.write("\n".join(LIST))
f.close()

f = open("OUT",'w')
sh = process("./client")
time.sleep(1)
i = 0
sh.recvline()
sh.recvline()
sh.recvline()
sh.sendline("arm")
sh.recvline()
for s in LIST[1:]:
    sh.sendline(s)
    resp = sh.recvline()
    f.write("%d %s" % (i,resp))
    if "SUCCESS" in resp:
        print i
        exit()
    i += 1
exit()

sh.sendline('1234')
sh.recvline()
time.sleep(2)
exit()
myInput = open("INPUT",'r')
myOutput = open("OUTPUT",'w')
p = subprocess.Popen(["./client"],stdin=myInput,stdout=myOutput)
myInput.close()
myOutput.close()
f = open("OUTPUT",'r')
i = 0
for line in f:
    if "Enter" in line:
        print line.count("Enter")
f.close()
