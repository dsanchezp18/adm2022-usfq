# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 11:55:36 2021

@author: Daniel Sanchez
"""
import pandas as pd # para importar los datasets
import matplotlib.pyplot as plt # para hacer gráficos
import scipy 
from scipy import stats

# Más en gráficos, otro script para que no se demore tanto

# creamos un dataset con solo precios de un solo ticker.

facebook=pd.read_excel('FB.xlsx') # a partir de los que creamos anteriormente

# separamos el tipo de precios para poder compararlos

fb_close=facebook['Adj Close']
fb_closae=facebook['Close']

# ahora sí un gráfico de boxplot 
bplt_fb=plt.figure() # esto es para que no se se sobreescriban los gráficos. 
plt.boxplot(fb_close)
plt.show()

# ahora uno comparando ambos precios
bplt_fb1=plt.figure()
plt.boxplot(facebook[['Adj Close', 'Close']])

# sacamos los precios de TWTR
twitter=pd.read_excel('TWTR.xlsx')
twitter_c=twitter['Close']
twitter_a=twitter['Adj Close']

# histograma
hist_twtr=plt.figure()
plt.hist(twitter_c, 100, color='black')
plt.title('Histograma Twitter Close Price', fontsize=18, fontname='Serif', color="blue")
plt.xlabel('Precio USD')
plt.ylabel('Frecuencia')

# histograma con frecuencias relativas, o gráfico de la PDF
hist_twtrr=plt.figure()
plt.hist(twitter_c, 100, color='black', density=True)
plt.title('Histograma Twitter Close Price', fontsize=18, fontname='Serif', color="blue")
plt.xlabel('Precio USD')
plt.ylabel('Frecuencia Relativa/Probabilidad')

# histograma de frecuencia acumulada, o gráfico de la CDF
hist_twtrrc=plt.figure()
plt.hist(twitter_c, 100, color='black', density=True, cumulative=True)
plt.title('Histograma Twitter Close Price', fontsize=18, fontname='Serif', color="blue")
plt.xlabel('Precio USD')
plt.ylabel('Frecuencia Relativa/Probabilidad')

# scatter plot
sct_1=plt.figure()
plt.scatter(fb_close, twitter_c)
plt.title('Scatter FB vs. TWTR', fontsize=18, fontname='Serif', color='purple')
plt.xlabel('FB')
plt.ylabel('TWTR')

# doble scatter plot

sct_2=plt.figure()
plt.scatter(fb_close, twitter_c, label='FB vs TWTR')
plt.scatter(twitter_c, fb_close, label='TWTR vs FB')
plt.xlabel('FB')
plt.ylabel('TWTR')
plt.legend()
plt.show()

# Un gráfico 3D

aapl_c = pd.read_excel('AAPL.xlsx')['Close']

fig=plt.figure()
plt.ax1=fig.add_subplot(111, projection='3d') 
# 111 son subdivisiones del cuadrante, 1 para cada eje por ende gráfico es normal
# eje x,y, y cuantos graficos hay en ese canvas
plt.ax1.scatter(fb_close, aapl_c, twitter_c)
plt.ax1.set_xlabel('FB')
plt.ax1.set_ylabel('AAPL')
plt.ax1.set_zlabel('TWTR')
plt.title('3D: FB, AAPL, TWTR')
plt.show()

# para regresiones

x=range(len(aapl_c)) # es el rango de los precios de AAPL, es una serie (t)
# len cuenta el número de elementos
# range pone en una serie desde 0 hasta el máximo de esa variable

slope,intercept,r2,pvalue,sterr=stats.linregress(x,aapl_c)
print(slope)
print(r2)

# Deber: mostrar gráficos de relaciones de acciones solo si su beta es mayor a 0.5
