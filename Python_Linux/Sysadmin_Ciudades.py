# Pide al usuario nombre de ciudades y escríbelas en un fichero de texto (el nombre se lo tienes que pedir también) hasta que el usuario introduzca un 0.
# Autor: Rocio Alzas Conde.
# Fecha: 21/02/2024

nom_fich= input("Introduce el nombre de un fichero: ")
fich_ciud=open(nom_fich,"w")
nom_ciud="-1"

while nom_ciud != "0":
    nom_ciud=input("Introduce nombre de ciudades: ")
    if nom_ciud != "0":
        fich_ciud.writelines(f"{nom_ciud}\n")