# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 11:04:22 2021

@author: Daniel Sanchez
"""

# Problema de Transporte

import pulp
import lp

# Coeficientes objetivo:
    
coef=[8,5,6,15,10,12,3,9,10]
lhs=[[1,0,0,1,0,0,1,0,0],[0,1,0,0,1,0,0,1,0],[0,0,1,0,0,1,0,0,1], [1,1,1,0,0,0,0,0,0],
     [0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,1,1,1]]
rhs=[150,70,60,100,100,80]
ILP_solution, objective_value=lp.ILP(coef,lhs,rhs,'','min')

