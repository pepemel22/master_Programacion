from string import Template

template = Template("El ")
msg = template.substitute(price="450")
print(msg)

# ---------------------------------------------------
# Resultado:                                        |
# --------------------------------------------------|
# El precio total es de 450$                        |
# ---------------------------------------------------

template = Template("El plural de $word es ${word}s ")
msg = template.substitute(word="moneda")
print(msg)

# ---------------------------------------------------
# Resultado:                                        |
# --------------------------------------------------|
# El plural de moneda es monedas                    |
# ---------------------------------------------------
