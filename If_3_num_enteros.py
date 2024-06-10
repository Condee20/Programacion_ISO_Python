# Leer tres números enteros y, si el primero de ellos es negativo, calcular el producto de los tres, en caso contrario calcular la suma de ellos.
# Autor: Rocio Alzas Conde.
# Fecha: 06/02/2024.

num_1=int(input("Introduce el primer número: "))
num_2=int(input("Introduce el segundo número: "))
num_3=int(input("Introduce el tercer número: "))

if num_1 < 0:
    mul = num_1 * num_2 * num_3
    print("El calculo de los productos es", mul)
elif num_1 > 0:
    sum = num_1 + num_2 +num_3
    print("El calculo de los productos es", sum)