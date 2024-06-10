# Tabla de multiplicar de todos los números. (Del 1 al 10).
# Autor: Rocío Alzas Conde.
# Fecha: 14/02/2024.

for i in range(1,11):
    print( "Tabla de multiplicar del",i,":")
    for j in range(1, 11):
        resultado = i * j
        print( i,"x",j, "=", resultado,)