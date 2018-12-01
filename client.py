#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 20:33:46 2018

@author: genius
"""
#client part
import socket

HOST = "localhost" # удаленный компьютер (localhost)
PORT = 9090 # порт на удаленном компьютере
msg=str()
while msg!='exit':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    msg=input(": ")
    sock.send(msg.encode("utf-8"))
    result = sock.recv(1024).decode("utf-8")
    if result==msg:
        print("Message accept")
    sock.close()
print("Server - ", result)
