# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 16:03:38 2021

@author: Daniel Sanchez
"""
# Repaso de importación de bases
# Primero utilizo la librería

import pandas as pd
import statistics as st
# ahora sí la base
df1=pd.read_excel('compras2021.xlsx')

# operaciones con las bases
mean_pricevat=st.mean(df1['Precio+IVA'])
sd_pricevat=st.stdev(df1['Precio+IVA'])

# reemplazando un número de una columna de la dataframe
df1['Precio+IVA'].replace(69.99,70,inplace=True)
print(df1.head())


