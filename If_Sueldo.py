# Dado el sueldo de un trabajador, aplique un aumento del 15% si su sueldo es inferior a $1000. Imprima el sueldo que percibirá.
# Autor: Rocio Alzas Conde.
# Fecha: 06/02/2024.

sueldo = int(input("Pon el sueldo que recibes: "))

if sueldo < 1000:
    subida= sueldo*1.15
    print("Ha recibido una subide del 15% por lo que su sueldo ahora es", subida)
else:
    print("No recibe la subida dado que su sueldo es mayor o igual a 1000.")