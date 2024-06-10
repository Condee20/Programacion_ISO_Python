# Programa que declare tres listas ‘lista1’, ‘lista2’ y ‘lista3’ de cinco enteros cada uno, pida valores para ‘lista1’ y ‘lista2’ y calcule lista3=lista1+lista2.
# Autor: Rocio Alzas Conde.
# Fecha: 19/02/2024.

lista1=[]
lista2=[]
lista3=[]

for i in range(0,5):
    num1=int(input("Introduce los número de la lista 1: "))
    lista1.append(num1)
    num2 = int(input("Introduce los número de la lista 2: "))
    lista2.append(num2)

for k in range(len(lista1)):
    lista3.append(lista1[k]+lista2[k])

print(lista3)