from string import Template

# ------------------------ASIGNACIÓN DE VARIABLES Y TEMPLATE ------------------------#
students = [
    ("Jana", 92, "matemáticas"),
    ("Carla", 94, "física"),
    ("Luis", 82, "biología"),
]

template = Template("Hola $name, tu nota final en $subject es: $punctuation")

# --------------------- FIN ASIGNACIÓN DE VARIABLES Y TEMPLATE ---------------------#

for i in students:
    print(template.substitute(name=i[0], punctuation=i[1], subject=i[2]))

# ---------------------------------------------------
# Resultado:                                        |
# --------------------------------------------------|
# Hola Jana, tu nota final en matemáticas es: 92    |
# Hola Carla, tu nota final en física es: 94        |
# Hola Luis, tu nota final en biología es: 82       |
# ---------------------------------------------------

for i in students:
    print(template.substitute(name=i[0], punctuation=i[1]))

# ---------------------------------------------------
# Resultado:                                        |
# --------------------------------------------------|
# Resultado: KeyError: 'subject'                    |
# ---------------------------------------------------

for i in students:
    print(template.safe_substitute(name=i[0], punctuation=i[1]))

# ---------------------------------------------------
# Resultado:                                        |
# --------------------------------------------------|
# Hola Jana, tu nota final en $subject es: 92       |
# Hola Carla, tu nota final en $subject es: 94      |
# Hola Luis, tu nota final en $subject es: 82       |
# ---------------------------------------------------
