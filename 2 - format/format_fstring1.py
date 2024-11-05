number1 = 10
number2 = 4

# -------------------------------------------------------------

print(f"El doble del número {number1} es {number1*2}")

# Resultado:
# El doble del número 10 es 20

# -------------------------------------------------------------

print(f"El número es {number1} {'mayor' if number1>5 else 'menor'} que 5")
print(f"El número es {number2} {'mayor' if number2>5 else 'menor'} que 5")

# Resultado:
# El número es 10 mayor que 5
# El número es 4 menor que 5

# -------------------------------------------------------------


def converter(km):
    return km * 1000


print(f"10 kilómetros son {converter(10):,} metros")

# Resultado:
# 10 kilómetros son 10,000 metros

# -------------------------------------------------------------

hello = "           Hola           "
print(f"{hello.strip()} Mundo")
print(f"{hello.lstrip()} Mundo")
print(f"{hello.rstrip()} Mundo")

# Resultado:
# Hola Mundo
# Hola            Mundo
#            Hola Mundo

# -------------------------------------------------------------