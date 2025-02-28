# Diccionarios

punto = {"x": 25, "y": 50}

print(punto)

print(punto["x"])  # imprime el valor de la clave x
print(punto["y"])  # imprime el valor de la clave y

punto["z"] = 45  # crea una nueva clave z con el valor 45

print(punto)
print(punto["z"])  # imprime el valor de la clave z

# print(punto["w"]) # error, la clave w no existe
# para evitar el error anterior, se puede usar el método get

print("w" in punto)  # imprime False, la clave w no existe

print(punto.get("w"))  # imprime None, la clave w no existe

punto["w"] = 100

if "w" in punto:
    print("Encontre la 'w'", punto["w"], punto)


print(punto.get("z"))  # imprime 45, la clave z existe

print("x" in punto)  # imprime True, la clave x existe

print(punto.get("v", -100))  # si la clave v no existe, imprime -100

del punto["z"]  # elimina la clave z

print(punto)

del (punto["w"])  # elimina la clave w

print(punto)

punto["z"] = 45
punto["w"] = 100

for clave in punto:  # imprime las claves
    print(f"{clave}: {punto[clave]}")


for valor in punto.values():  # imprime los valores
    print(valor)

for clave in punto.keys():  # imprime las claves
    print(clave)

for valor in punto.items():  # imprime clave y valor como tupla
    print(valor)

for clave, valor in punto.items():  # imprime clave y valor
    print(f"{clave}: {valor}")


usuarios = [
    {"id": 1, "primer nombre": "Johnnatan",
        "segundo nombre": "", "apellido": "Villaneda"},
    {"id": 2, "primer nombre": "Edier",
        "segundo nombre": "Andres", "apellido": "Villaneda"},
    {"id": 3, "primer nombre": "Angelica",
        "segundo nombre": "Janeth", "apellido": "Bocanegra"},
    {"id": 4, "primer nombre": "Kelly",
        "segundo nombre": "Johana", "apellido": "Murillas"},
    {"id": 5, "primer nombre": "Lina",
        "segundo nombre": "Marcela", "apellido": "Murillas"},
]


for usuario in usuarios:
    if usuario["segundo nombre"] != "":
        print(f"{usuario['id']}: {usuario['primer nombre']} {
              usuario['segundo nombre']} {usuario['apellido']}")
    else:
        print(f"{usuario['primer nombre']} {
              usuario['apellido']}")
