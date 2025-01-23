# Keywords arguments
def get_product(**datos):
    print(datos["id"], datos["name"])


get_product(id="19", name="Samsung", desc="Celular")
