# Crea una lista e inicialízala con 5 cadenas de caracteres leídas por teclado. Copia los elementos de la lista en otra lista, pero en orden inverso, y muestra sus elementos por la pantalla.
# Autor: Rocio Alzas Conde.
# Fecha: 16/02/2024

list1=[]
list2=[]

for i in range(5):
    caracter=input("Introduce un caracter: ")
    list1.append(caracter)

list2=list1.copy()
list2.reverse()

print(list1)
print(list2)