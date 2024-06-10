# Crea una lista con los meses del año, pide números al usuario, si el numero está entre 1 y la longitud máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de error.
# El programa termina cuando el usuario introduce un cero.
# Autor: Rocío Alzas Conde.
# Fecha: 19/02/2024

list_mes=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]

while True:
    num_mes=int(input("Introduce un número: "))
    if 1 <= num_mes <= 12:
        mes = list_mes[num_mes - 1]
        print(mes)
    elif num_mes == 0:
        break
    else:
        print("Introduce un número válido.")