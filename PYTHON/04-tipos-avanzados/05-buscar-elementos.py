mascotas = ["Pelusa", "Tomas", "Pulga", "Tomas", "Simon"]

nombre = "Tomas"

print(mascotas.count(nombre))  # 2

if "Tomas" in mascotas:
    print(f"{nombre} está en la lista")
    print(mascotas.index(nombre))  # 1


print(mascotas.count("Pelusa"))  # 1

if "Pelusa" in mascotas:
    print("Pelusa está en la lista")
    print(mascotas.index("Pelusa"))  # 0
