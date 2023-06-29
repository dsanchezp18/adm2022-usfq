# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 11:51:12 2021

@author: mango
"""

# Importamos las librerías necesarias

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly as py # requiere de pip install
import plotly.graph_objs as go
from sklearn.cluster import KMeans
from plotly.offline import plot

# Importar un archivo csv
df=pd.read_csv('Clients.csv')

# Vamos a crear clusters de clientes con información de edad, ingreso, y calificación de gastos

cluster_data=df[['Age','Annual Income (k$)','Spending Score (1-100)']]
algorithm=KMeans(n_clusters=5)
algorithm.fit(cluster_data)

# Para que python nos muestre los clusters
labels_1=algorithm.labels_ 
print(labels_1) # a que cluster pertenece cada cliente en la base de datos

# Para ver los centroids
centroids1=algorithm.cluster_centers_
print(centroids1)

# Lo pongo en el dataframe al mapeo de cada cluster
df['labels']=labels_1

# nueva librería para el gráfico

trace1=go.Scatter3d(
    x=df['Age'],
    y=df['Annual Income (k$)'],
    z=df['Spending Score (1-100)'],
    mode='markers',
    marker=dict(color=df['labels'], size=10, line=dict(color=df['labels'], width=12), opacity=0.8),
       )
data=[trace1]
layout=go.Layout(title='Segmentación de Mercado con K-Means',
                 scene=dict(xaxis=dict(title='Edad')
                            ,yaxis=dict(title='Ingreso Anual'),
                            zaxis=dict(title='Gasto')
                            ))
fig=go.Figure(data=data,layout=layout)
plot(fig)