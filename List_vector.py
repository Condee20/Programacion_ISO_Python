# Programa que declare una lista y la vaya llenando de números hasta que introduzcamos un número negativo. Entonces se debe imprimir el vector (sólo los elementos introducidos).
# Autor: Rocio Alzas Conde.
# Fecha: 16/02/2024

list=[]
num=0

while True:
    num=int(input("Introduce un número: "))
    if num >= 0:
        list.append(num)
        continue
    else:
        break

print("La lista de números introducidos es :", list)