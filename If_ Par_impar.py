# Se desea leer por teclado un número comprendido entre 0 y 10 (inclusive) y se desea visualizar si el número es par o impar.
# Autor: Rocio Alzas Conde.
# Fecha: 06/02/2024.

num= int(input("Introduce un número: "))

if num >= 0 and num <= 10:
    if num%2 == 0:
        print("El número", num,"es par.")
    else:
        print("El número", num,"es impar.")
else:
    exit("No has introducido un número entre 0 y 10")