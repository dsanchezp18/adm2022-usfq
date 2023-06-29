# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 16:55:03 2021

@author: Daniel Sanchez
"""

import datetime as dt # para que python cache las fechas
import matplotlib.pyplot as plt # para hacer gráficos
import matplotlib.dates as mdates # porsiacaso
import pandas as pd # para pandas importar datos
import pandas_datareader.data as web 
import numpy as np
import os
import sys

# Script para sacar precios de diferentes empresas
start=dt.datetime(2013,3,1) # definimos una fecha de inicio del periodo
end=dt.datetime(2021,3,23)
 
tickerlist=['AAPL', 'FB', 'TSLA','F']
# aqui sacamos un solo dataframe con los datos de todas las firmas
df_somefirms=web.DataReader(tickerlist, 'yahoo', start, end)
print(df_somefirms)

df_somefirms.to_excel('somefirmsprice.xlsx')
# se demora una eternidad hacer este codigo largo
