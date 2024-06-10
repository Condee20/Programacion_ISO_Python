# Dada una cadena de texto, indique el número de vocales que tiene.
# Autor: Rocío Alzas Conde.
# Fecha: 09/02/2024.

palabra=input("Introduce una palabra: ")
i=0

for letra in palabra:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        i=i+1

print("El número de vocales de", palabra,"es", i)
