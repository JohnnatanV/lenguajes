def producto(a, b):
    resultado = a * b
    return (resultado)


a = producto(2, 3)
b = producto(4, 5)
c = producto(3, 5)
d = producto(c, 2)

# print(a)
# print(b)
print(d)


def get_datos(**datos):
    return (datos["id"], datos["name"], datos["desc"])


resultado = get_datos(id=35, name="Johnnatan", desc="Ingeniero")

print(resultado)
