# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 19:50:18 2021

@author: Daniel Sanchez
"""

import matplotlib.pyplot as plt # para hacer graficos
import random as rnd # para numeros aleatorios
import pandas as pd # para importar bases csv

df = pd.read_csv (r'C:\Users\Daniel Sanchez\OneDrive\Documentos\u\u9\operaciones\python\world_small.csv')
print(df)
a=[rnd.randint(0,700),rnd.randint(0,700),rnd.randint(0,700),rnd.randint(0,700),rnd.randint(0,700),rnd.randint(0,700)]

plt.boxplot(a)
plt.boxplot(df.gdppcap08)

df_gspc=pd.read_csv (r'C:\Users\Daniel Sanchez\OneDrive\Documentos\u\u9\operaciones\python\^GSPC.csv')

plt.boxplot(df_gspc.High)