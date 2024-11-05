txt1 = "Me llamo {name}, tengo {age} años".format(name="Miguel", age=57)
txt2 = "Me llamo {0}, tengo {1} años".format("Miguel", 57)
txt3 = "Me llamo {}, tengo {} años".format("Miguel", 57)
txt4 = "Tengo {1} años. Me llamo {0}".format("Miguel", 57)
txt5 = "Tengo {age} años. Me llamo {name}".format(name="Miguel", age=57)

print(txt1)
print(txt2)
print(txt3)
print(txt4)
print(txt5)

# Resultado:
# Me llamo Miguel, tengo 57 años
# Me llamo Miguel, tengo 57 años
# Me llamo Miguel, tengo 57 años
# Tengo 57 años. Me llamo Miguel
# Tengo 57 años. Me llamo Miguel

# ------------------------------------------------------

hours = 24
calls = 120
msg = "Hemos recibido {llamadas} llamadas en {horas} horas"
print(msg.format(llamadas=calls, horas=hours))

# ------------------------------------------------------
