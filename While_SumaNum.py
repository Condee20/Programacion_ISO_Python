# Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la suma de todos los números positivos ingresados.
# Autor: Rocio Alzas Conde.
# Fecha: 07/02/2024.

total=0
i=1

while i!=0:
    i=int(input("Introduzca un número: "))
    if i>0:
        total=total+i
        continue
print("La suma de los números es: ", total)