# Calculadora con Match
# Autor: Rocío Alzas Conde.
# Fecha: 07/02/2024.

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
oper = input("Introduce la operación a realizar (+,-,* o /): ")

match oper:
    case "+":
        resul = num1 + num2
    case "-":
        resul = num1 - num2
    case "*":
        resul = num1 * num2
    case "/":
        resul = num1 / num2
    case _:
        print("No has introducido ninguna opción.")

print("El resultado de la suma entre", num1, "y", num2, "es", resul)
