# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 10:39:51 2020

@author: Sarang
This is the COURSERA assigment
"""

import re

file= input("Enter File Name: ")
sumdigit=0
li=list()
hand=open(file)
for line in hand:
    digit=re.findall('[0-9]+', line)
    for di in digit:
        di.split()
        d=di.rstrip()
        dig=int(di)
        sumdigit = sumdigit + dig
print(sumdigit)
    
