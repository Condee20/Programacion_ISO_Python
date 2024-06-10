# Abre el fichero de usuarios en Linux y muestra la información del usuario que se solicite únicamente. Si el usuario no existe, se muestra un mensaje de error.
# Autor: Rocio Alzas Conde.
# Fecha: 21/02/2024

fich_users=open("/etc/passwd","r")

lineas=fich_users.readlines()
busc_user=input("Introduce un usuario: ")

for i in lineas:
    if busc_user in i:
        print("Se ha encontrado el usuario.")
        print(i)
    else:
        print("No se ha encontrado el usuario.")
        break

fich_users.close()