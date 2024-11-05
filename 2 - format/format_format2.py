txt1 = " Quedan: {:<10} plazas libres en la planta 1"
txt2 = " Quedan: {:<10} plazas libres en la planta 2"
txt3 = " Quedan: {:<10} plazas libres en la planta 3"

print(txt1.format(50))
print(txt2.format(80))
print(txt3.format(95))

# Resultado ---------------------------------------#
#  Quedan: 50         plazas libres en la planta 1 |
#  Quedan: 80         plazas libres en la planta 2 |
#  Quedan: 95         plazas libres en la planta 3 |
# -------------------------------------------------#

txt1 = " Quedan: {:>10} plazas libres en la planta 1"
txt2 = " Quedan: {:>10} plazas libres en la planta 2"
txt3 = " Quedan: {:>10} plazas libres en la planta 3"

print(txt1.format(50))
print(txt2.format(80))
print(txt3.format(95))

# Resultado ---------------------------------------#
# Quedan:         50 plazas libres en la planta 1  |
# Quedan:         80 plazas libres en la planta 2  |
# Quedan:         95 plazas libres en la planta 3  |
# -------------------------------------------------#
