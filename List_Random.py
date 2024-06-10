# Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.
# Autor: Rocío Alzas Conde.
# Fecha: 1402/2024.

import random as r

numeros=[]

for i in range(0,10):
    num = r.randint(1, 10)
    numeros.append(num)

for i in range(0,10):
    numeros[i]
    print("El elemento",numeros[i], "es al cuadrado",numeros[i]*numeros[i],"y al cubo",numeros[i]*numeros[i]*numeros[i])