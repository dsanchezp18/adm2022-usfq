# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 10:34:22 2021

@author: Daniel Sanchez
"""
# Creamos listas para importar en el script de intro

def sumado(z):
    suma_z=0
    for i in z:
        suma_z=suma_z+i
    return suma_z

def promediado (b):
    #calcular la suma 
    sumatoria=0
    for i in b:
        sumatoria=sumatoria+i
        
    #contar los elementos
    n=len(b)
    # divido la suma para n 
    promedio=sumatoria/n
    
    #print promedio
    print ('el promedio de la lista es igual a {}'. format(promedio))
    
    return promedio


