data = {"nombre": "Lucía", "edad": 22}
msg = "Hola, {nombre}. Tienes {edad} años.".format_map(data)
print(msg)

# Resultado: "Hola, Lucía. Tienes 22 años."

# --------------------------------------------------#

profession = {
    "name": ["Antonio", "Lucas", "Julia"],
    "profession": ["abogado", "doctor", "programadora"],
    "age": [30, 31, 28],
}

for i in range(len(profession["name"])):
    print(
        "{name} es {profession} y tiene {age} años.".format(
            name=profession["name"][i],
            profession=profession["profession"][i],
            age=profession["age"][i],
        )
    )

# Resultado:
# Antonio es abogado y tiene 30 años.
# Lucas es doctor y tiene 31 años.
# Julia es programadora y tiene 28 años.
