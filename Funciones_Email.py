# Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje indicando si la dirección es válida o no, valiéndose de una función para decidirlo. Una dirección se considerará válida si contiene el símbolo "@“
# Autor: Rocio Alzas Conde.
# Fecha: 20/02/2024

def email(a):
    arro=0
    for i in a:
        if i == "@":
            arro=arro+1
    if arro == 1:
        print("Es una dirección valida.")
    else:
        print("Es una dirección no válida.")

dir_email=input("Introduce una dirección email: ")
email(dir_email)