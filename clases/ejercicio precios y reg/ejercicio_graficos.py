# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 10:28:02 2021

@author: Daniel Sanchez
"""

# Trabajo: graficar series de tiempo de precios SP500 solo si su beta es mayor a 0.5


# Primero importamos las librerías necesarias.

import pandas as pd # para importar los datasets
import pandas_datareader.data as web # para descargarse cosas de forma automática
# esta librería necesita hacer pip install pulp
import matplotlib.pyplot as plt # para hacer gráficos
import scipy # para regresiones
from scipy import stats # mas aún de regresiones
import datetime as dt # manejo de fechas
import numpy as py # para estadísticas y similares

# Importamos un archivo de Excel con tickers

sp=pd.read_excel('SP500.xlsx')

# Definir un período de tiempo
start=dt.datetime(2016,3, 27)
end=dt.datetime(2021,3,27)

# Saco solamente los tickers
sp_tickers=sp['firm']

# Automatizamos la bajada de información para cada uno de los 500 tickers
# Utilizamos un for loop que busca la info y luego exporta esa info a un archivo de Excel

for firm in sp_tickers :
    df=web.DataReader(firm,'yahoo', start, end)
    df.to_excel('./files/{}.xlsx'.format(firm))

# creo una dataframe para cada ticker en la lista, y le nombro como su ticker dentro de la carpeta files
# que está dentro del WD, por eso uso el punto
# format va poniendo para cada nombre su firm correspondiente
   
    # solamente selecciona la columna close de cada uno de esos
    price=df['Close']
    
    # para cada empresa hacemos una regresión: price~t
    t=range(len(price)) # sacamos un vector que es una serie aritmetica de los períodos para cada precio
    slope, intercept, r2, p, se=stats.linregress(t,price) #calculo regresiones
    
    # Verificar si el beta es mayor que 0.5 n
    if slope > 0.5:
        # hacer scatter plot
        fig=plt.figure # para que se guarde en uno solo
        plt.scatter(t,price)
        plt.title('Regresión de {} vs el tiempo'.format(firm))
        plt.ylabel('Precio al cierre')
        plt.xlabel('Días')
        plt.show()
    


