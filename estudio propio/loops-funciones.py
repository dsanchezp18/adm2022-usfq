# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 15:15:57 2021

@author: Daniel Sanchez
"""
# Para probar loops
b=range(0,100000)  # Genera una secuencia del 0 al 1000000
print(b) # range object, osea resume la secuencia, no es como R
sumatoria=0
for i in b:
    sumatoria=sumatoria+i
print(sumatoria)
# Verificando: 
sum(range(0,100000))

def average (x):
    # calcular la suma primero: 
    sigmax=0
    for i in x:
        sigmax=sigmax+i
    n=len(x)
    averageof=sigmax/n
    print('the list averages to {}'.format(averageof))
    return(averageof)
# definir una lista a ser promediada
lista=range(151,15931202)

# usar la función mean de python
# necesito primero importar la librería

import statistics
average(lista)
average_comp=statistics.mean(lista)
print("{:.2f}".format(average_comp))
