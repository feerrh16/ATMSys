def pagar_servicio(usuario):
    print("Pago de servicios")
    servicios = {"1": "Luz", "2": "Agua", "3": "Gas"}
    for key, value in servicios.items():
        print(f"{key}. {value}")
    opcion = input("Seleccione el servicio a pagar: ")
    if opcion in servicios:
        cantidad = int(input("Ingrese la cantidad a pagar: "))
        # Aquí se debería actualizar el saldo y registrar el pago en la base de datos
        print(f"Pago de {servicios[opcion]} de ${cantidad} exitoso")
    else:
        print("Opción no válida")

# Agregar la lógica de conexión a la base de datos aquí
# Solo deje los servicios de Luz, Agua y Gas, no se si se debia agregar Telefono/Internet, Me avisas

