# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 15:50:51 2021

@author: Daniel Sanchez
"""

# Primero el más simple: un ifelse
a=645
b=56454
if a<b:
    print('{} es menor que {}'.format(a,b))
else: 
    print('{} es mayor o igual que {}'.format(a,b))

# Ahora uno más cagado: if mas elif

f=1532
d=1532
if f<d:
    print('{} es menor que {}'.format(f,d))
elif f==d:
    print('{} es igual que {}'.format(f,d))
elif f>d: 
    print('{} es mayor que {}'.format(f,d))

u=153214513626
w=153251
if u<w:
    print('{} es menor que {}'.format(u,w))
elif u==w:
    print('{} es igual que {}'.format(u,w))
elif u>w: 
    