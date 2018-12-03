#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 15:50:18 2018

@author: genius
"""
#server part
import socket
from func import *

HOST = host(__file__) # enter to localhost
PORT = 9090
srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

srv.bind((HOST, PORT))
msg=str()

while msg!='exit':
    print("Слушаю порт: "+ str(PORT))
    srv.listen(1)
    sock, addr = srv.accept()
    print("Connect accept to " + str(addr))

    while msg!='exit':
        tmp = sock.recv(1024)
        if not tmp:
            break
        msg = tmp.decode("utf-8")
        print("Loop at %s:%s" % addr, msg)
        sock.send(msg.encode("utf-8"))

    sock.close()
