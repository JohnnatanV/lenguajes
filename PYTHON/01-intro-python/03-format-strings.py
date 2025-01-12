animal = "luna"
animal2 = "UmI"
estado = "   estoy debiendo Plata       "
print(animal.upper())
print(animal.lower())
print(animal2.capitalize())
print(estado.title())
print(estado.strip())
print(estado.strip().title())
print(estado.lstrip())
print(estado.rstrip())
print(estado.find("es"))
print(estado.find("$"))
print(estado.strip().find("es"))
print(estado.replace("estoy", "No estoy"))
print("Pl" in estado)
print("Pl" not in estado)
print("Pa" in estado)
