# Debéis de crear un script en Python que tenga un menú con 4 opciones. El programa acaba cuando se introduce la opción 4. Se debe comprobar que el usuario que ejecuta el script es el root.
# ▪ Opción 1: Muestra información del SSOO e información de la CPU.
# ▪ Opción 2: Pedir un usuario. Si existe, se muestra información sobre él, si no, se crea.
# ▪ Opción 3: Pedir al usuario un directorio. Comprobar si existe y si es un directorio, en caso contrario, lo crea.
# ▪ Opción 4: Salir.
# Autor: Rocío Alzas Conde.
# Fecha: 26/02/2024.

import os
import cpuinfo as c


def ssoo():
    print("Información del dispositivo:")
    print(f"Sistema operativo: {os.uname()}")
    print("GPU: ",c.get_cpu_info()["brand_raw"])

def user():
    fich_users = open("/etc/passwd", "r")
    encon=False
    usuario = input("Introduce un usuario: ")
    for i in fich_users:
        if usuario in i:
            encon=True
    if encon == True:
        print("El usuario "+usuario+" ya existe")
    else:
        print("No se ha encontrado el usuario.")
        os.system("useradd -m " + usuario)
        print("Se ha creado el usuario " + usuario)

    fich_users.close()

def directorio():
    dir_rut=input("Introduce un directorio: ")
    if os.path.exists(dir_rut):
        if os.path.isdir(dir_rut):
            print("El directorio "+dir_rut+ " ya existe.")
        else:
            print("El directorio "+dir_rut+" no es un directorio.")
    else:
        print("El directorio ingresado no existe, vamos a proceder a crearlo.")
        os.mkdir(dir_rut)
        print("El directorio "+dir_rut+" creado exitosamente.")

while True:
    print("--------------------------------")
    print("Menú de 4 opciones:")
    print("1.- Mostrar información de SSOO.")
    print("2.- Buscar usuario.")
    print("3.- Buscar un directorio.")
    print("4.- Salir")
    print("--------------------------------")
    op=int(input("Escoge una de las opciones: "))

    match op:
        case 1:
            ssoo()
        case 2:
            user()
        case 3:
            directorio()
        case 4:
            exit("Has escogido la opción de salir.")
        case _:
            print("Vuelve a leer las opciones y escoge una de ellas.")