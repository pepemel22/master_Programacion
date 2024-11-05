name = "Miguel"
age = 57
PI = 3.141592
number = 255
num_exp = 12345.6789
discount = 25


msg = "Hola, %s" % name
print(msg)
# Resultado: "Hola, Miguel"

msg = "Me llamo, %s y tengo %d años." % (name, age)
print(msg)
# Resultado: "Me llamo, Miguel y tengo 57 años"

msg = "El valor del número PI es: %f " % PI
print(msg)
# Resultado: "El valor del número PI es: 3.141592"

msg = "El valor del número PI es: %.4f " % PI
print(msg)
# Resultado: "El valor del número PI es: 3.1416"

msg = "En hexadecimal, el número 255 es: %x o %X " % (number, number)
print(msg)
# Resultado: "En hexadecimal, el número 255 es: ff o FF"

msg = "Y en octal, el mismo número es: %o " % number
print(msg)
# Resultado: "Y en octal, el mismo número es: 377"

msg = "La notación científica del número 12345.6789 es: %e o %E " % (num_exp, num_exp)
print(msg)
# Resultado: "La notación científica del número 12345.6789 es: 1.234568e+04 o 1.234568E+04"

msg = "Le hizo un descuento del %d%%" % discount
print(msg)
# Resultado: "Le hizo un descuento del 25%"
