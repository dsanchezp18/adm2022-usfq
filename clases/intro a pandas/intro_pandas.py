# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 11:00:52 2021

@author: Daniel Sanchez
"""
# Introducción a pandas

# No llamar al archivo pandas porque causa conflicto el rato que Python busca la librería. 

import pandas as pd #en vez de llamarle a pandas así, solo debo escribir con pd
import numpy as np
# libreria tiene funciones ya creadas para hacer cosas, por ejemplo para importar hojas de excel o csv 

df=pd.read_excel('Info.xlsx') # poner nombre exacto y además con la extensión de archivo
# pandas se le llama y con punto llamamos a la función, en este caso es como read.csv
# es una variable tipo dataframe, como una hoja de excel en python, una base de datos

df.dropna(inplace=True) # para dataframes, dropna saca las filas que tengan algun missing o NA

# reemplazar la variable df con la que se hace después de la limpieza de datos con inplaceT
# sobreescribe la variable df
# no se ha sobreeescrito nada de nuestro archivo en excel, solo la variable en python

# para reemplazar a los NA's con otros variables
df.replace(np.nan, 'hola', inplace=True) 
# primero digo que quiero reemplazar, uso esta otra librería numpy

# para reemplazar algo de una columna en específico
df['Fondo'].replace(1,1000,inplace=True) #el nombre la columna funciona como índice

# para guardar una nueva variable
fondo=df['Fondo'] # es la extracción de nuevos subsets
print(fondo)

fondomonto=df[['Fondo', 'Monto']]
print(fondomonto) # para sacar varias columnas, es decir crear una lista. 

df['Euros']= df['Monto']*1.21 # para crear nuevas columnas dentro del dataframe
print(df)
# para sacar columnas que no quiero tener
df.drop('Euros','columns',inplace=True) # keyword columns le dice a python donde es que debe borrar
print(df)
df.drop(1,'rows',inplace=True)

# agregar filtros, crear subsets con condiciones

x=df[df['Monto']>200]
print(x)

y=df[df['Año']==2012]
print(df)

# exportar información a Excel

y.to_excel('2012.xlsx')

