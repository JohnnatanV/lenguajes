mascotas = ["Killer", "Lucifer", "Judas", "Cremita"]

# for mascota in mascotas:
#   print(mascota)


# print(mascotas[3])

mascotas[3] = "Vainilla"

# print(mascotas)
# print(mascotas[3])

# print(mascotas[-1])

# print(mascotas[1:4:2])


numeros = list(range(21))
numeros2 = list(range(1, 21))

print("nuermos_1", numeros[3:10])

print("numeros_2", numeros[5:])

print("numeros_3", numeros[:19])

print("numeros_4", numeros[-10])

print("numeros_5", numeros[::2])  # Numeros pares

print("numeros_6", numeros[2::])

# Todos los caminos llevan a roma, mas de un metodo para obtener el mismo resultado
print("numeros_7.1 impares", numeros[1::2])  # numeros impares

print("numeors_7.2 impares", numeros2[::2])  # numeros impares


###

print("numeros_8", numeros[2:19:4])


def printer():
    print("printer", list(range(11)))


printer()
