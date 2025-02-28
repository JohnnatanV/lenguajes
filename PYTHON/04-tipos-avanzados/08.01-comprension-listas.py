usuarios = [["Chancho", 2], ["Umi", 1], ["Lucifer", 5],
            ["Emilio", 3], ["Sir Bigotes Ronroneantes", 4]]

nombres = []

for usuario in usuarios:
    nombres.append(usuario[0])

# print("for", nombres)


# map
# nombres = [expresion for item in items]
nombres = [usuario[0] for usuario in usuarios]
print("lista transformada", nombres)

# filter
# nombres = expresion for item in items if condicion
nombres = [usuario for usuario in usuarios if usuario[1] > 2]
print("lista filtrada", nombres)

# nombres = expresion for item in items if condicion
nombres = [usuario[0] for usuario in usuarios if usuario[1] > 3]
print("lista filtrada y tranformada", nombres)

contenido = list(map(lambda usuario: usuario, usuarios))
print("contenido map: ", contenido)

nombres = list(map(lambda usuario: usuario[0], usuarios))

print("nombres map: ", nombres)

menosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))

print("menosUsuarios filter: ", menosUsuarios)
