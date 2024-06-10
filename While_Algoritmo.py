# Crear un algortimo que le pregunte al usuario cuantos número quiere introducir. Pedir los números y ver si son par o impar.
# Autor: Rocio Alzas Conde.
# Fecha: 07/02/2024.

cant=int(input("¿Cuántos númeor quieres introducir? "))
i=0

while True:
    num = int(input("Introduce un número: "))
    i +=1
    if i == cant:
        print("Has llegado al último número.")
        break