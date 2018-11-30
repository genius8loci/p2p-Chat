#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 15:50:18 2018

@author: genius
"""

import socket


#server part
sock = socket.socket()
sock.bind(('', 9090))
sock.listen(10)
now, addr = sock.accept()

print('connected:', addr)

while True:
    now.settimeout(30)
    data = now.recv(16384)
    data = data.decode("utf-8")
    if not data:
        print("No data")
        now.close()
        break
    print(": "+ data)


input()
