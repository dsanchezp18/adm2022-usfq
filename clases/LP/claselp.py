# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 22:10:36 2021

@author: Daniel Sanchez
"""

# Resolviendo Problemas de LP con Python
# Tiene el beneficio de que no se tiene límitaciones

import pulp
import lp

coefs=[0.6,0.1, 0.09] # Coeficientes de la función objetivo a maximizar
lhs=[[1, 0.15,0.045], [0.375,0.05,0.045], [1,0,0], [0,1,0],[0,0,1]] # Coeficientes de restricciones
# Debe ser una matriz, similar a como se ve en Excel
# Para eso usamos listas dentro de listas con corchetes. Cada uno es una fila
# No deben empezarse nombres de objetos con mayúsculas
rhs=[175,180,100,1400,1000] # Lista con los valores totales/límites de cada restricción

ILP_solution, objective_value=lp.ILP(coefs,lhs,rhs,'','max')


