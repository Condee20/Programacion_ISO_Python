# Escriba una función en Python que reproduzca lo siguiente: 𝑓(𝑥, 𝑦) = 𝑥2 + 𝑦2
# Autor: Rocio Alzas Conde.
# Fecha: 20/02/2024

def fun(x,y):
    res=x**2+y**2
    return res

a=int(input("Introduce un número: "))
b=int(input("Introduce un número: "))

res = fun(a, b)
print(f"El resultado de ({a}, {b}) es: {res}")