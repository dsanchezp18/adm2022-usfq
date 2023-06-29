# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 22:48:05 2021

@author: mango
"""

# Algoritmo ML para empresas: hacer clusters para empresas en base a diferentes variables: 
# Variables a considerar: volumen, precio open y precio close
# Scatter plot con cuatro clusters al 3d, con diferentes colores cada uno

# Primero importamos nuestras librerías

import pandas as pd # para manejo de dataframes
import numpy as np
import datetime as dt # para utilizar las fechas
import matplotlib.pyplot as plt
import seaborn as sns
import plotly as py # requiere de pip install
import plotly.graph_objs as go
from sklearn.cluster import KMeans
from plotly.offline import plot
import pandas_datareader.data as web # para la automatización de descargas
import os

# importamos una lista de las empresas en el s&p500

firms=pd.read_excel('SP500.xlsx')

# sacamos solo la lista de tickers de las firmas
df=firms['firm']

# ahora hay que definir fechas para el intervalo que queremos hacer. utilizaremos precios del 1 de abril 2021

start=dt.datetime(2021,3,26) #year, month, day
end=dt.datetime(2021,3,26) 

# automatización de la bajada de datos de un dataframe que solo tiene los tickers de las empresas.

# utilizamos un for loop para sacar excels de todas las companias en la lista

for i in df :
    data_firms=web.DataReader(i,'yahoo',start,end)
    data_firms.to_excel('{}.xlsx'.format(i))
    
# debemos leer todos los exceles en esa carpeta que creamos, y luego listarlos para poder unirlos

# creamos una variable que lista los nombres de todos los files en una carpeta dada
# esto se hace con la librería OS
cwd=os.path.abspath('')
file_names=os.listdir(cwd)

# ahora un loop que lee todos y los une
df_all=pd.DataFrame()
for file in file_names:
    if file.endswith('.xlsx'):
        df_all=df_all.append(pd.read_excel(file), ignore_index=True)

df_all.to_excel('entero.xlsx')






