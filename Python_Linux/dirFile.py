# Dado un fichero denominado rutas.txt, que contiene el nombre de ficheros y directorios que ya deben existir, introducir en 2 listas diferentes cada uno de ellos, es decir, en una lista los ficheros y en otra los directorios (habrá que comprobar línea a línea si lo leído es un fichero o un directorio). Posteriormente, se le pedirá al usuario qué elija una opción:
# A- Pedir nombre de fichero y eliminarlo.
# B- Pedir nombre de directorio y mostrar su información.
# C- Pedir nombre de fichero, nombre de destino y copiarlo en dicho destino.
# D- Mostrar lista elegida por el usuario
# E- Salir
# Autor: Rocío Alzas Conde.
# Fecha: 01/03/2024.

import shutil
import os


def Fichero():
    Fich = input("Introduce la ruta fichero: ")
    if os.path.exists(Fich):
        os.remove(Fich)
        print("Se ha eliminado el fichero correctamente.")
    else:
        print("El fichero no existe.")


def Directorio():
    Dir = input("Introduce un directorio: ")
    if os.path.exists(Dir):
        if os.path.isdir(Dir):
            print(f"La informaciín de {Dir} es:")
            print(os.listdir(Dir))
        else:
            print(f"El directorio {Dir} no existe.")


def Copiar():
    Fich = input("Introduce un fichero: ")
    Dir2 = input("Introduce el directorio en el que lo quieres copiar: ")
    shutil.copy(Fich, Dir2)
    print("El fichero se ha copiado perfectamente.")


def Lista():
    ruta = open("rutas.txt", 'r')
    fichero = []
    directorio = []
    lineas = ruta.readlines()

    for i in lineas:
        r=i.strip()
        if os.path.isfile(r):
            fichero.append(r)
        elif os.path.isdir(r):
            directorio.append(r)

    print("Mostrar listas:")
    print("1.- Mostrar lista de ficheros.")
    print("2.- Mostrar lista de directorios.")
    List_mos = input("Introduce la lista quieres mostrar: ")
    if List_mos == '1':
        print(fichero)
    if List_mos == '2':
        print(directorio)
    ruta.close()


while True:
    print("---------------------------------------------------------------------------")
    print("Menú")
    print("A - Pedir nombre de fichero y eliminarlo.")
    print("B - Pedir nombre de directorio y mostrar su información.")
    print("C - Pedir nombre de fichero, nombre de destino y copiarlo en dicho destino.")
    print("D - Mostrar lista elegida por el usuario.")
    print("E - Salir.")
    print("---------------------------------------------------------------------------")
    op = input("Introduce una de las opciones mencionadas: ")

    match op:
        case 'A':
            Fichero()
        case 'B':
            Directorio()
        case 'C':
            Copiar()
        case 'D':
            Lista()
        case 'E':
            exit("Has escogido la opción E. Vas a salir del programa.")