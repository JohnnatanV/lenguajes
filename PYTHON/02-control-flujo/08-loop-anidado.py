for j in range(3):  # inicia arriba primera vuelta -> Segunda vuelta pasa al siguente rango -> Tecera vuelta pasa al ultimo valor del rango
    for k in range(2):  # Segundo paso, ejecuta el loop en el rango -> En la segunda vuelta repite el loop en el rango -> En la tercera vuelta repite el loop en el rango
        print(f"j={j}, k={k}")
