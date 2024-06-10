# Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.
# Autor: Rocio Alzas Conde.
# Fecha: 20/02/2024

def es_palindromo(a):
    list_1=[]
    list_2=[]
    for i in pal:
        list_1.append(i)
        list_2.append(i)
    list_1.reverse()
    if list_1==list_2:
        print("Es un palindromo.")
    else:
        print("No es un palindromo.")

pal=input("Introduce una palabra: ")
es_palindromo(pal)


