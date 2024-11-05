number_1 = 0.1
number_2 = 0.2

print(f"{ number_1 + number_2 =}")

# Resultado:
# number_1 + number_2 =0.30000000000000004

# ----------------------------------------------------------------------------------------------#
# Python (y la mayoría de los lenguajes de programación) utiliza el estándar IEEE 754           #
# para representar los números en punto flotante. Este estándar usa una representación          #
# binaria para almacenar estos números. No todos los números decimales se pueden                #
# representar de forma exacta en binario, ya que algunos requieren una cantidad infinita        #
# de bits para ser representados.                                                               #
# En el caso de 0.1 y 0.2, sus representaciones en binario son periódicas                       #
# (es decir, tienen infinitas cifras después del punto), lo que significa que deben ser         #
# truncadas para poder ser almacenadas en memoria.                                              #
# Como resultado, cuando realizas operaciones con estos números, el resultado puede tener       #
# pequeñas imprecisiones.                                                                       #
# --------------------------------------------------------------------------------------------- #

print(f"{ number_1 + number_2 = :.2f}")

# Resultado:
# number_1 + number_2 =0.30