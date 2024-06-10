# Elaborar un algoritmo que permita ingresar el número de partidos ganados, perdidos y empatados, por un club en la liga, se debe de mostrar su puntaje total, teniendo en cuenta que por cada partido ganado obtendrá 3 puntos, empatado 1 punto y perdido 0 puntos.
# Autor: Rocío Alzas Conde.
# Fecha: 05/02/2024.

ganados=int(input("Introduce los partidos ganados: "))
perdidos=int(input("Introduce los partidos perdidos: "))
empates=int(input("Introduce los partidos empatados: "))

pun_ganados= ganados*3
pun_empates= empates*1

puntuacion= pun_ganados+pun_empates

print("La puntuación total del equipo es ", puntuacion)