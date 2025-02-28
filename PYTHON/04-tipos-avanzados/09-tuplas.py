# Tuplas

numeros = (1, 2, 3, 4, 5)
numeros_2 = numeros + (6, 7, 8, 9, 0)

print(numeros)
print(numeros_2)

# numeros.append(10)  # Error
# print(numeros)

punto = tuple([1, 2])

print(punto)


menosNumeros = numeros[:3]
print(menosNumeros)

primero, segundo, *resto = numeros
print(primero, segundo, *resto)

for n in numeros:
    print(n)


listaNumeros = list(numeros)

listaNumeros[2] = "El Barto"

print(listaNumeros)
