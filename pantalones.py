#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 07:04:32 2022

@author: jonathansoto
"""

#declaración 
pantalones = 0
descuentos = 0

#lectura de datos
pantalones = int( input("Ingrese el num de pantalones \n") )

#operaciones
if(pantalones < 5):
    print("no hay descuento")
    print("Total: ", pantalones*200)
    
if(pantalones >= 5 and pantalones < 12):
    descuentos = 200 * 0.15;
    print("12% de descuento")
    print("Total: ", pantalones* (200-descuentos))
    
if(pantalones >= 12):
    descuentos = 200 * 0.30
    print("30% de descuento")
    print("Total: ", pantalones *(200 - descuentos) )
  
    
  
    