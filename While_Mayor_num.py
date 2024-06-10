# Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Mostrar cuál fue el mayor número ingresado
# Autor: Rocio Alzas Conde.
# Fecha: 07/02/2024.

num=0
i=1

while i!=0:
    i=int(input("Introduzca un número: "))
    if i > num:
        num=i
print("El número mayor es: ", num)