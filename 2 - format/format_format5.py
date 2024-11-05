number = 255
PI = 3.14159265
discount = 0.25

msg = " El número {:d} convertido a binario es: {:b}"
print(msg.format(number, number))

# Resultado:
# El número 255 convertido a binario es: 11111111

msg = " El número {:d} convertido a octal es: {:o}"
print(msg.format(number, number))

# Resultado:
# El número 255 convertido a octal es: 377

msg = " El número {:d} convertido a hexadecimal es: {:x} o {:X}"
print(msg.format(number, number, number))

# Resultado:
# El número 255 convertido a hexadecimal es: ff o FF

msg = " El número {:d} convertido a formato científico es: {:e}"
print(msg.format(number, number))
msg = " El número {:d} convertido a formato científico es: {:E}"
print(msg.format(number, number))

# Resultado:
# El número 255 convertido a formato científico es: 2.550000e+02
# El número 255 convertido a formato científico es: 2.550000E+02

msg = "El número PI es igual a: {:f}"
print(msg.format(PI))

msg = "El número PI es igual a: {:.2f}"
print(msg.format(PI))

msg = "El número PI es igual a: {:.8f}"
print(msg.format(PI))

# Resultado:
# El número PI es igual a: 3.141593
# El número PI es igual a: 3.14
# El número PI es igual a: 3.14159265

msg = "El descuento sobre el precio es de un {:%}"
print(msg.format(discount))

msg = "El descuento sobre el precio es de un {:.2%}"
print(msg.format(discount))

msg = "El descuento sobre el precio es de un {:.0%}"
print(msg.format(discount))

# Resultado
# El descuento sobre el precio es de un 25.000000%
# El descuento sobre el precio es de un 25.00%
# El descuento sobre el precio es de un 25%
