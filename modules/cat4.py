#Tool Name :- Tool-X v2.0 
# Author :- Rajkumar Dusad
# Date :- 1/11/2017
# Aex Software's :- Tool-X is a automatic tool installer. Specially made for termux and GNURoot Debian terminal.

import os
import sys
from time import sleep
from core.system import *
from logo import *

def inst():
	os.system("cd .tools && python2 .inst.aex")

def inst1():
	os.system("cd .tools && python2 .inst1.aex")

def cat4():
	os.system("clear")
	cat4_logo()

	Toolo = raw_input("\n\033[1;33m >>>  \033[1;m")
	if Toolo == "1":
		usr=open(".tools/uip.aex","w")
		usr.write("20")
		usr.close()
		inst()
	elif Toolo == "2":
		usr=open(".tools/uip.aex","w")
		usr.write("19")
		usr.close()
		inst()
	elif Toolo == "3":
		usr=open(".tools/uip.aex","w")
		usr.write("65")
		usr.close()
		inst()
	elif Toolo == "4":
		usr=open(".tools/uip.aex","w")
		usr.write("23")
		usr.close()
		inst()
	elif Toolo == "5":
		usr=open(".tools/uip.aex","w")
		usr.write("47")
		usr.close()
		inst()
	elif Toolo == "6":
		usr=open(".tools/uip.aex","w")
		usr.write("145")
		usr.close()
		inst()
	elif Toolo == "7":
		usr=open(".tools/uip.aex","w")
		usr.write("146")
		usr.close()
		inst()
	elif Toolo == "8":
		usr=open(".tools/uip.aex","w")
		usr.write("147")
		usr.close()
		inst()
	elif Toolo == "9":
		usr=open(".tools/uip.aex","w")
		usr.write("148")
		usr.close()
		inst()
	elif Toolo == "00" or Toolo=="back":
		pass
	else:
		print ("\033[01;34m\007\n error : \033[01;37m\'"+Toolo+"\' \033[01;31minvalid option !!!")
		sleep(1)
		cat4()
