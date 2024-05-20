def depositar_efectivo(usuario):
    print("Depósito de efectivo")
    cantidad = int(input("Ingrese la cantidad a depositar (múltiplos de 100): "))
    if cantidad % 100 == 0 and 100 <= cantidad <= 10000:
        # Aquí se debería actualizar el saldo en la base de datos y validar los billetes
        print(f"Depósito de ${cantidad} exitoso")
    else:
        print("Cantidad no válida. Debe ser un múltiplo de 100 entre 100 y 10000")

# De nuevo aqui sigue con el codigo de la conexion
