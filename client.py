#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 20:33:46 2018

@author: genius
"""
#client part
import socket
from func import *
import time
import os

check()

HOST = host(os.path.basename(__file__)) # удаленный компьютер (localhost)
PORT = 9090 # порт на удаленном компьютере

server = startServer()
time.sleep(5)
msg=str()
while msg!='exit':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    time.sleep(1)
    while True:
        msg=input(": ")
        if msg:
            break
    sock.send(msg.encode("utf-8"))
    result = sock.recv(1024).decode("utf-8")
    if result==msg:
        print("Message accept")
    sock.close()
print("Server - ", result)
