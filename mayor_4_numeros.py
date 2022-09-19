#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 07:04:32 2022

@author: jonathansoto
"""

#declaración 
num1 = 0
num2 = 0
num3 = 0
num4 = 0

#lectura de datos

num1 = int( input("Num1:") )
num2 = int( input("Num2:") )
num3 = int( input("Num3:") )
num4 = int( input("Num4:") )

#operaciones

if(num1 > num2 and num1 > num3 and num1 > num4):
    print(num1)
    
if(num2 > num1 and num2 > num3 and num2 > num4):
    print(num2)
    
if(num3 > num2 and num3 > num1 and num3 > num4):
    print(num3)
    
if(num4 > num2 and num4 > num3 and num4 > num1):
    print(num4)
    