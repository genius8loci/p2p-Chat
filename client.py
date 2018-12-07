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
from colorama import *

init()
check()

HOST = host()                # удаленный компьютер (localhost)
PORT = 9090                                     #порт на удаленном компьютере

server = startServer()                          #start subprocess server
time.sleep(5)                                   #waiting to startServer
msg=str()

while msg!='exit':                              #quit chat, write "exit"
    print(Style.RESET_ALL, end='')
    print(Style.BRIGHT, end='')

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    time.sleep(1)

    #print("")                                   #need for "\003[A:"
    while True:
        msg=input(Back.RED + "\n: ")
        if msg:
            break
    sock.send(msg.encode("utf-8"))              #send message

    result = sock.recv(1024).decode("utf-8")    #server response
    if result==msg:                             #if it is the same, it becomes green
        confirm(msg)

    sock.close()
print("Server - ", result)
