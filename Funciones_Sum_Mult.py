# Escribir una funcion sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
# Autor: Rocio Alzas Conde.
# Fecha: 20/02/2024

list_num = [1, 2, 3, 4]

def sumar_lista(lista):
    suma = 0
    for i in lista:
        suma += i
    return suma

def multiplicar_lista(lista):
    multiplicacion = 1
    for i in lista:
        multiplicacion *= i
    return multiplicacion

ressum = sumar_lista(list_num)
resmult = multiplicar_lista(list_num)

print(f"La suma de la lista {list_num} es: {ressum}")
print("--------------------------------")
print(f"El producto de la lista {list_num} es: {resmult}")