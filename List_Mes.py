# Crea un programa que pida un número al usuario un número de mes (por ejemplo, el 4) y diga cuántos días tiene (por ejemplo, 30) y el nombre del mes. Debes usar listas. Para simplificarlo vamos a suponer que febrero tiene 28 días.
# Autor: Rocio Alzas Conde.
# Fecha: 19/02/2024.

meses=[
        {"nombre": "Enero", "dias": 31},
        {"nombre": "Febrero", "dias": 28},
        {"nombre": "Marzo", "dias": 31},
        {"nombre": "Abril", "dias": 30},
        {"nombre": "Mayo", "dias": 31},
        {"nombre": "Junio", "dias": 30},
        {"nombre": "Julio", "dias": 31},
        {"nombre": "Agosto", "dias": 31},
        {"nombre": "Septiembre", "dias": 30},
        {"nombre": "Octubre", "dias": 31},
        {"nombre": "Noviembre", "dias": 30},
        {"nombre": "Diciembre", "dias": 31},]

num_mes=int(input("Introduce el número del mes que quieres: "))

if 1 <= num_mes <= 12:
    mes = meses[num_mes - 1]
    print(f"El mes {num_mes} es {mes['nombre']} y tiene {mes['dias']} días.")
else:
    print("Introduce un número válido.")