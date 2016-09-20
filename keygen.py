from pwn import *
import time
import os


current = subprocess.Popen(["date","+%s"],stdout=subprocess.PIPE)
(out,err) = current.communicate()

now = int(out)

f = open("key",'r')
info = f.read()
spoof = ""

while open("1651565998.key",'r').read() != info:
    now -= 1
    os.system("sudo date +%%s -s @%d" % now)
    subprocess.Popen(["./keygen",'-g','-k','1651565998','-o','master'])

print "TIME: %d WORKS!" % now

#os.system("sudo service ntp stop")
#os.system("sudo ntpdate -s time.nist.gov")
#os.system("service ntp start")
