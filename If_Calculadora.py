# Realiza una calculadora que pida al usuario la opción que desea y pida dos números y muestre el resultado.
# Autor: Rocio Alzas Conde.
# Fecha: 06/02/2024.

num_1=int(input("Introduce el primer número: "))
num_2=int(input("Introduce el segundo número: "))
cont=input("Introduce la cuenta que quieres hacer (S, R, D o M): ")

if cont == "S":
    resul_s = num_1 + num_2
    print("El resultado de la suma es", resul_s)
elif cont == "R":
    resul_r = num_1 - num_2
    print("El resultado de la resta es", resul_r)
elif cont == "D":
    resul_d = num_1 / num_2
    print("El resulado de la división es", resul_d)
elif cont == "M":
    resul_m = num_1 * num_2
    print("El resultado de la multiplicación es", resul_m)