# Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10). A continuación, debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor.
# Autor: Rocio Alzas Conde.
# Fecha: 16/02/2024

list_notas=[]

nota_min=11
nota_max=0

for i in range(5):
    notas=int(input("Introduce la nota (0,10): "))
    list_notas.append(notas)

for i in list_notas:
    if i > nota_max:
        nota_max=i

    if i < nota_min:
        nota_min = i

print("Notas:", list_notas)

nota_media = sum(list_notas) / len(list_notas)
print("Nota media: ", nota_media)

print("Nota más alta:",nota_max)
print("Nota más baja:" ,nota_min)