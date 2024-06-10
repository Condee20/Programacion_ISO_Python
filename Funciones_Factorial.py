# Escribir un programa que pida números al usuario hasta que ingrese 0, mostrar el factorial de cada uno y, al finalizar, la cantidad total de números leídos en total. Utilizar una o más funciones, según sea necesario.
# Autor: Rocio Alzas Conde.
# Fecha: 20/02/2024

def fac():
    while True:
        num = int(input("Introduce un número: "))
        i = 1
        fact = 1
        if num == 0:
            break
        elif num > 0:
            while i <= num:
                fact = fact * i
                i = i + 1
        print("La factorial de", num, "es", fact)

fac()