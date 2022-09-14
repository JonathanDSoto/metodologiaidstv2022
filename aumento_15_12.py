#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 07:04:32 2022

@author: jonathansoto
"""

#declaración 
sueldo = 0
aumento = 0

#lectura de datos
sueldo = int( input("Ingrese su sueldo \n") )

#operaciones
if( sueldo < 5000 ):
    aumento = sueldo * 0.15
    
    print("El sueldo es de: ", sueldo + aumento)
    
else:
    aumento = sueldo * 0.12
    
    print("El sueldo es de: ", sueldo + aumento)
    
  
    
  
    
  
    