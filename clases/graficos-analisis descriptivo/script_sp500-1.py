# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 10:20:01 2021

@author: Daniel Sanchezb
"""

import datetime as dt  # para que python cache las fechas
import matplotlib.pyplot as plt  # para hacer gráficos
import pandas as pd  # para pandas importar datos
import pandas_datareader.data as web

# cuando haya errores en importacion hay que instalar así como el pulp
# anaconda prompt<- pip.install.pulp
# en el caso de data reader, es pip install pandas-datareader

# Vamos a buscar y visualizar precios de acciones de una empresa para un período dado

start=dt.datetime(2016,3,1) # definimos una fecha de inicio del periodo
end=dt.datetime(2021,3,1) # definimos la fecha de finalización del período

FBtick='FB' # ticker de la empresa para la cual debo buscar datos 

# busquemos en python la información de precios, se puede en una línea de código

df_FB=web.DataReader(FBtick, 'yahoo', start, end) # buscar info de ciertas fuentes
df_FB.to_excel('facebook.xlsx')

df_AAPL=web.DataReader('AAPL', 'yahoo',start,end)
df_AAPL.to_excel('apple.xlsx')

# con una lista de firmas podemos hacer lo mismo

some_firms= ['FB', 'AAPL', 'TWTR']

# para sacar diferentes excels para cada firma: un for loop

for i in some_firms:
    df_loop=web.DataReader(i, 'yahoo', start, end) # saco para cada firma 
    df_loop.to_excel('{}.xlsx'.format(i)) 
 
# construyo un excel para cada uno, el nombre es ticker
    
# estadísticos básicos para un dataframe 

estad=df_FB.describe() # crea primero los estadísticos en python
estad.to_excel('estad_FB.xlsx') # los exportamos a Excel
print(estad)
# Ahora sí el primer gráfico
# Caja y bigotes del precio de AAPL

# para que no se sobreescriba el gráfico, debemos generar un objeto con el grafico
bpapl1=plt.figure()
plt.boxplot(df_AAPL['Adj Close'])
plt.show()

# ahora un histograma
bpapl2=plt.figure()
plt.hist(df_AAPL['Adj Close'], 100) # 100 intervalos

# para otro histograma pero ahora con tuiter
TWTR_p=pd.read_excel('TWTR.xlsx')
twtrplt=plt.figure()
plt.hist(TWTR_p['Close'], 100)
plt.show()

