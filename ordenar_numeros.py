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

#lectura de datos
num1 = int( input("Ingrese el valor") )
num2 = int( input("Ingrese el valor") )
num3 = int( input("Ingrese el valor") )

#operaciones

#1 buscar al más pequeño
if(num1 < num2 and num1 < num3):
    print(num1)
if(num2 < num1 and num2 < num3):
    print(num2)
if(num3 < num2 and num3 < num1):
    print(num3)
    
#3 buscar el de enmedio
if(num1 > num2 and num1 < num3):
    print(num1)
if(num1 < num2 and num1 > num3):
    print(num1)
    
if(num2 > num1 and num2 < num3):
    print(num2)
if(num2 < num1 and num2 > num3):
    print(num2)

if(num3 > num1 and num3 < num2 ):
    print(num3)
if(num3 < num1 and num3 > num2):
    print(num3)

#2 buscar el más grande 
if(num1 > num2 and num1 > num3):
    print(num1)
if(num2 > num1 and num2 > num3):
    print(num2)
if(num3 > num2 and num3 > num1):
    print(num3)
 



    