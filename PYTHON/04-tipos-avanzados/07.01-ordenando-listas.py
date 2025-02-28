numeros = [2, 9, 0, 19, 83, 12, 1, 90, 1001, -1]

# ordena la lista por el residuo de la división entre 10
numeros.sort(key=lambda x: x % 10)

usuarios_1 = [[2, "Chancho"], [1, "Umi"], [5, "Lucifer"],
              [3, "Emilio"], [4, "Sir Bigotes Ronroneantes"]]

usuarios = [["Chancho", 2], ["Umi", 1], ["Lucifer", 5],
            ["Emilio", 3], ["Sir Bigotes Ronroneantes", 4]]


usuarios.sort(key=lambda parametros: parametros[1])
print(usuarios)

# ordena la lista por el segundo elemento de cada sublista
usuarios.sort(key=lambda x: x[1])

# ordena la lista por el segundo elemento de cada sublista de mayor a menor
usuarios.sort(key=lambda x: x[1], reverse=True)

# ordena la lista por el primer elemento de cada sublista
usuarios.sort(key=lambda x: x[0])

# ordena la lista por el primer elemento de cada sublista de mayor a menor
usuarios.sort(key=lambda x: x[0], reverse=True)

# ordena la lista por la longitud del segundo elemento de cada sublista
usuarios_1.sort(key=lambda x: len(x[1]))
