# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 10:37:21 2021

@author: mango
"""
print(2+2)
a=1 #el asignador es el igual, los nombres de las variables no pueden empezar con numeros
# no se puede tampoco poner asignadores nombres con espacio
mi_nombre="daniel"
print(mi_nombre) # se necesita siempre esto para poder verle en la consola
b=67
#str  te convierte a texto una variable, type te dice de que tipo es 
# + para CONCATENAR textos, y sumar numeros
print(a+b)
print(str(b)+mi_nombre) # hay que convertir igual todo a texto

# format es para ingresar argumentos dentro de oraciones, 
# automaticamente hace las transformaciones de tipo de texto
# int es para transformar a numero
day=1
month="febrero"
year="2021"
print(str(day)+' '+'de'+' '+month+' '+'de'+' '+str(year))

print('hoy es {} de {} del {}'.format(day,month,year))
# importante mantener el orden de la fecha, python no va a detectar.
# Ejemplo: 
    
uno="hola"
dos="soy"
tres="equis"

print('{} hola {} el {}'.format(uno, dos, tres))

# indices:  
 
a=[1,'dos','hola',4]
print(a)
print(len(a))
# len es la función para devolver el largo de la función. 

# para pedirle un elemento
print(a[1]) #0 siempre es el primer elemento en toda lista.
g=[5,[1,'dos','hola',4],132,66]
print(g[1][3]) # el cuarto elemento del segundo elemento
#dos corchetes es para meterse dentro de las listas en las listas.


b=[1,2,3,4,5,6,7,8,9, 10]
print('este es el elemento {}'.format(b[0]))
print('este es el elemento {}'.format(b[1]))
print('este es el elemento {}'.format(b[2]))
print('este es el elemento {}'.format(b[3]))
 
# automatizamos la tarea con un loop
for i in b: #para cada i en el vector o lista b, i toma un valor, en orden
 #es un iterable
    print('este es el elemento {}'.format(i))

# Sumar todos los valores de una lista, sin importar el numero de elementos que tenga
sigma=0 # definimos un lugar para guardar la suma
for i in b:
    sigma=sigma+i #guarda las sumas en cada una de las iteraciones, al final vale todo
    # haciendole que se refiera a si mismo cogemos el elemento de la anterior iteración
print (sigma) # imprime el valor de la variable al 

# funcionará con cual sea el numero de elementos en una
 
# Haciendo un algoritmo para el promedio de una lista

mu=0 # lista para meter las cosas
n=len(b) # cuenta el número de elementos en el objeto a contar
print(sigma/n) # calcula el promedio

# definiendo funciones creamos una función que hace el promedio
def promediar (b):
    # calcular la suma 
    sumatoria=0
    for i in b:
        sumatoria=sumatoria+i
    # contar los elementos
    n=len(b)
    # divido la suma para n 
    promedio=sumatoria/n
    # print promedio
    print ('el promedio de la lista es igual a {}'. format(promedio))
    
    return promedio

a=[2451251,51256,1612363,2,626,2534.525125171261,161,36,1361,36,16,16]
promedio_a=promediar(a)
print(promedio_a)
print(round(promedio_a,2))

#definir una variable para sumar
def sumar(z):
    suma_z=0
    for i in z:
        suma_z=suma_z+i
    return(suma_z)
d=[15,26,512, 61,23.21]
resultado_d=sumar(d)
print(resultado_d)
print('La sumatoria de la lista es igual a {}'. format(resultado_d))

# Podemos crear funciones en otros scripts e importarles a este script. 

import suma_prom # sacando de un diferente script, no debe estar abierto solo en la misma carpeta o WD

resd=suma_prom.sumado(d)


# Otro tipo de loops: while loops

# repite una serie de comandos hasta que la condición sea falsa
a=0
b=1
while a < b:
    print('a es menor que b (while)')
    a=b*2
print (a)
# imprime una vez y luego hace lo siguiente, la condición deja de ser verdad. 
# imprime a al final del proceso
# for loop repite un número especifico de veces, esta vez los ciclos no son definidos, sino la condición.
# en el for loop, un iterable define el número de ciclos. 
# si es que la condición nunca deja de ser verdad, el loop es infinito


# condicionales: 
if a < b: #la primera parte de un bloque de condicionales
    print ('a es menor que b')

# ahora elif es para definir las siguientes condiciones 
# logicas a ser probadas en el bloque de condicionales
elif a==b: #dos iguales compara variables para condiciones lógicas
    print ('a es igual que b')

elif a > b:
    print ('a es mayor que b')

# un ifelse, considera la primera condicion y luego todo e++l resto como el complemento

if a < b: 
    print ('a es menor que b')
else: 
    print ('otras condiciones')
    
a=0
if a < b and a==0:  # and necesita que se cumplan ambas condiciones en esta linea. 
    print ('a menor que b y 0')
else: 
    print (' a no es diferente')

# no revisamos ninguna condición que se haga con elif despues de que la primera condición sea verdadera. 

import pulp # no hay errores

# para verificar que instalamos bien niseque cosa