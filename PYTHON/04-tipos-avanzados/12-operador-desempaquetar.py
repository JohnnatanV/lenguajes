# Operador Desempaquetador

lista = [1, 2, 3, 4]
lista_2 = (1, 2, 3, 4)

print(lista)  # imprime [1, 2, 3, 4]

print(1, 2, 3, 4)
print(*lista)  # imprime 1 2 3 4 con el operador desempaquetador *
print(*lista_2)  # imprime 1 2 3 4 con el operador desempaquetador *

lista_3 = [5, 6]

combinada = ["Hola", *lista, "Mundo", *lista_3, True]
print(combinada)  # imprime ['Hola', 1, 2, 3, 4, 'Mundo', 5, 6, True]

punto_1 = {"x": 15}
punto_2 = {"y": 25}
punto_3 = {"z": 35}

nuevo_punto = {**punto_1, **punto_2, **punto_3}

print(nuevo_punto)  # imprime {'x': 15, 'y': 25, 'z': 35}

punto_4 = {"z": 45, "aa": 100}
extra_punto = {"v": 45, "w": 55}

punto_diferente = {**punto_1, **punto_2, **punto_3, **punto_4, **extra_punto}
# imprime {'x': 15, 'y': 25, 'z': 45, 'aa': 100, 'v': 45, 'w': 55}
print(punto_diferente)
