# Se tiene los puntos A y B en el cuadrante positivo del plano cartesiano, elabore el algoritmo que permita obtener la distancia entre A y B.
# Autor: Rocio Alzas Conde.
# Fecha: 05/02/2024

A1=int(input("Introduce el punto A (x): "))
A2=int(input("Introduce el punto A (y): "))
B1=int(input("Introduce el punto B (x): "))
B2=int(input("Introduce el punto B (y): "))

distancia=((A1-B1)**2 + (A2-B2)**2)**0.5

print("La distancia entre el punto A y el punto B es", distancia)