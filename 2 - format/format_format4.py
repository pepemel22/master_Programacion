temp_min = -5
temp_max = 10

msg = "Las temperaturas de hoy oscilarán entre los {:-} grados de mínima y los {:-} grados de máxima"
print(msg.format(temp_min, temp_max))

# Resultado:
# Las temperaturas de hoy oscilarán entre los -5 grados de mínima y los 10 grados de máxima
# ------------------------------------------------------------------------------------------

d_sol = 1392700
msg = "El diámetro del Sol es de: {:_}km."
print(msg.format(d_sol))

msg = "El diámetro del Sol es de: {:,}km."
print(msg.format(d_sol))

# Resultado:
# El diámetro del Sol es de: 1_392_700km.
# El diámetro del Sol es de: 1,392,700km.
# ------------------------------------------------------------------------------------------
