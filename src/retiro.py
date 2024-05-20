def retirar_efectivo(usuario):
    print("Retiro de efectivo")
    cantidad = int(input("Ingrese la cantidad a retirar (múltiplos de 100): "))
    if cantidad % 100 == 0 and 100 <= cantidad <= 10000:
        # Aquí se debería actualizar el saldo en la base de datos
        print(f"Retiro de ${cantidad} exitoso")
    else:
        print("Cantidad no válida. Debe ser un múltiplo de 100 entre 100 y 10000")

# Aqui se agregara la logica de la conexion
