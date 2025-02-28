usuarios = [["Chancho", 2], ["Umi", 1], ["Lucifer", 5],
            ["Emilio", 3], ["Sir Bigotes Ronroneantes", 4]]

nombres = [
]

for usuario in usuarios:
    nombres.append(usuario[0])

print("for", nombres)

# nombres = [expresion for item in items]
nombres = [usuario[0] for usuario in usuarios]
print("lista transformada", nombres)

# nombres = [expresion for item in items if condicion]
nombres = [usuario for usuario in usuarios if usuario[1] > 3]
print("lista filtrada", nombres)


nombres = [usuario[0] for usuario in usuarios if usuario[1] > 3]
print("lista filtrada y tranformada", nombres)
