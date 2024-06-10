# Hacer un programa que inicialice una lista de números con valores aleatorios (10 valores), y posterior ordene los elementos de menor a mayor.
# Autor: Rocío Alzas Conde.
# Fecha: 19/02/2024.

import random as r

list=[]

for i in range(0,10):
    num = r.randint(1,10)
    list.append(num)
list.sort()
print("Esta en la lista ordenada de menor a mayor:",list)