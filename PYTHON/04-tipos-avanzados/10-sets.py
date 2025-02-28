# Set significa grupo o conjunto

primer = {1, 2, 3, 1, 4, 5, 2, 6}

print(primer)

primer.add(7)  # add() agrega un elemento al set

print(primer)

primer.remove(1)  # remove() remueve un elemento del set

print(primer)

segundo = [3, 4, 5, 8, 9]

segundo = set(segundo)  # Convierte una lista en un set

print(segundo)

print(primer | segundo)  # | une dos sets

print(primer.union(segundo))  # union() une dos sets

# intersection() muestra los elementos comunes
print(primer.intersection(segundo))

print(primer & segundo)  # & muestra los elementos comunes

# difference() muestra los elementos que no se repiten
print(primer.difference(segundo))

print(primer - segundo)  # - muestra los elementos que no se repiten

print(primer ^ segundo)  # ^ muestra los elementos que no se repiten


# print(segundo[2]) # set no soporta indexación

if 5 and 8 in segundo:
    print("Hola mundo!")
