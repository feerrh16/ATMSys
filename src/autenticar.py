def iniciar_sesion():
    tarjeta = input("Ingrese su número de tarjeta: ")
    pin = input("Ingrese su PIN: ")
    # Aquí se debería validar la tarjeta y el PIN con la base de datos
    # Esta es una implementación simplificada
    if tarjeta == "12345678" and pin == "1234":
        print("Autenticación exitosa")
        return {"tarjeta": tarjeta, "usuario": "Usuario Demo"}
    else:
        print("Autenticación fallida")
        return None

# Fer aqui debes agrefar la lógica de conexión a la base de datos