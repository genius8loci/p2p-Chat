#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 20:36:15 2018

@author: genius
p2p (not use server)
color text
my first chat
сheck ip
"""
import time


def host():
    with open("host.txt", "r+") as f:
        host = f.read()

        if host=='':
            f.write(input("IP your friend (enter to localhost): "))
            if host=='':
                f.write("localhost")
                f.close()
                return "localhost"
        if host!='':
            f.close()
            return host

print(host())
print(host())
print(host())
