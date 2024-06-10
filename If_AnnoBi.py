# Dada una variable year con un valor entero, compruebe si dicho año es bisiesto o no lo es. Un año es bisiesto en el calendario Gregoriano, si es divisible entre 4 y no divisible entre 100, o bien si es divisible entre 400.
# Autor: Rocio Alzas Conde.
# Fecha: 06/02/2024.

year=int(input("Introduce un año: "))

if (year%4 == 0 and year % 100 !=0) or (year % 400 == 0):
    print(year, "es un año bisiesto.")
else:
    print(year, "no es año bisiesto.")