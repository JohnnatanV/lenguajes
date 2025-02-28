mascotas = ["Pelusa", "Maggie", "Tomas", "Pulga", "Penelope", "Tomas", "Simon"]

mascotas.insert(1, "Whisky")  # indice, elemento
print(mascotas)

# inserta un elemento al final de la lista
mascotas.append("Ayudante de santa")
print(mascotas)

mascotas.remove("Tomas")  # Elimina la primera ocurrencia del elemento
print(mascotas)

mascotas.pop()  # Elimina el ultimo elemento de la lista
print(mascotas)

# Elimina el elemento en el indice indicado en este caso el segundo elemento
mascotas.pop(1)
print(mascotas)

del mascotas[0]  # Elimina el elemento en el indice indicado
print(mascotas)

mascotas.clear()  # Elimina todos los elementos de la lista
print(mascotas)
