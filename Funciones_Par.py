# Función que diga si un número es par o no.
# Autor: Rocio Alzas Conde.
# Fecha: 20/02/2024

def par(a):
    if a % 2 == 0:
        print("Es par.")
    else:
        print("Es impar.")

b=int(input("Introduce la cantidad de vese que quieres repetir: "))

for i in range(b):
    c=int(input("Introduce un número: "))
    par(c)