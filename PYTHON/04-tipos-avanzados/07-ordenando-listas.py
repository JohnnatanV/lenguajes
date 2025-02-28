numeros = [2, 9, 0, 19, 83, 12, 1, 90, 1001, -1]

numeros.sort()  # ordena la lista de menor a mayor
print("sort", numeros)

numeros.sort(reverse=True)  # ordena la lista de mayor a menor
print("sort:reverse=True", numeros)

numeros_2 = sorted(numeros)  # crea una nueva lista ordenada de menor a mayor
print("sorted", numeros_2)

# crea una nueva lista ordenada de mayor a menor
numeros_3 = sorted(numeros, reverse=True)
print("sorted:reverse=True", numeros_3)

usuarios_1 = [[2, "Chancho"], [1, "Umi"], [5, "Lucifer"],
              [3, "Emilio"], [4, "Sir Bigotes Ronroneantes"]]

usuarios_1.sort()
print("sort", usuarios_1)

usuarios = [["Chancho", 2], ["Umi", 1], ["Lucifer", 5],
            ["Emilio", 3], ["Sir Bigotes Ronroneantes", 4]]

usuarios.sort()
print("sort", usuarios)


def ordena(elemento):
    return (elemento[1])


usuarios.sort(key=ordena)
print("sort:key=ordena", usuarios)

usuarios.sort(key=ordena, reverse=True)
print("sort:key=ordena, reverse=True", usuarios)
