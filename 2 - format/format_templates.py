from string import Template

t = Template("Soy $name desde $city")
print("Plantilla = ", t.template)

# ---------------------------------------------------
# Resultado:                                        |
# --------------------------------------------------|
# Plantilla =  Soy $name desde $city                |
# ---------------------------------------------------

template = Template("El precio total es de $price$$")
msg = template.substitute(price="450")
print(msg)
