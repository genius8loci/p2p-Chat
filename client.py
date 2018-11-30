#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 20:33:46 2018

@author: genius
"""

import socket

#client part

sock = socket.socket()
sock.connect(('localhost', 9090))

#for msg in range(100):
msg = input(": ")
sock.send(msg.encode("utf-8"))

data = sock.recv(1024)

input()
sock.close()
