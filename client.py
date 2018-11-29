#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 15:50:18 2018

@author: genius
p2p (not use server)
color text
my first chat
сheck ip
"""

import socket


#server part
sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
now, addr = sock.accept()

print('connected:', addr)

while True:
    data = now.recv(1024)
    if not data:
        break
    print(": "+ data)

now.close()


print("He")