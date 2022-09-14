#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 07:04:32 2022

@author: jonathansoto
"""

#declaración 
monto = 0
descuento = 0

#lectura de datos
monto = int( input("Ingrese el monto \n") )

#operaciones
if(monto < 500):
    print("No hay descuento")
    
if(monto >= 500 and monto < 1000):
    descuento = monto * 0.5
    print("DEscuento de 5%")
    print("Total: ", monto - descuento)
    
if(monto >= 1000 and monto < 7000):
    descuento = monto * 0.11
    print("DEscuento de 11%")
    print("Total: ", monto - descuento)

if(monto >= 7000 and monto < 15000):
    descuento = monto * 0.18
    print("DEscuento de 18%")
    print("Total: ", monto - descuento)
  
if(monto >= 15000 ):
    descuento = monto * 0.25
    print("DEscuento de 25%")
    print("Total: ", monto - descuento)
    
  
    