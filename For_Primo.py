# Determinar si un número pedido por teclado es primo.
# Autor: Rocío Alzas Conde.
# Fecha: 14/02/2024.

num=int(input("Introduce un número: "))
cont=0

for i in range (1,num+1):
    if num % i == 0:
        cont=cont+1

if cont <= 2:
    print("El número", num, "es primo")
