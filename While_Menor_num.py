# Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Mostrar cuál fue el menor número ingresado
# Autor: Rocio Alzas Conde.
# Fecha: 07/02/2024.

men=999999
num=int(input("Introduzca un número: "))

while num != 0:
    if num < men:
            men = num
    num = int(input("Introduzca un número: "))
print("El número menor es:", men)