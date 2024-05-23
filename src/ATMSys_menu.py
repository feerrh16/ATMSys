from CajeroDAO import CajeroDAO
from ClienteDAO import ClienteDAO
from Cajero import Cajero
from Cliente import Cliente

def mostrar_menu():
    print("=== Menú Principal ===")
    print("1. Retiro en efectivo")
    print("2. Depósito de efectivo")
    print("3. Pago de tarjeta de crédito")
    print("4. Pago de servicios")
    print("5. Consulta de saldo")
    print("6. Consulta de movimientos")
    print("7. Salir")

def iniciar_sesion():
    cliente_dao = ClienteDAO()
    num_cliente = int(input("Ingrese su numero de cliente: "))

    clientes = ClienteDAO.seleccionar()
    cliente_encontrado = None

    for cliente in clientes:
        if cliente.id_persona == num_cliente:
            cliente_encontrado = cliente
        break

    if cliente_encontrado:
        print(f"Bienvenido {cliente_encontrado.nombre} {cliente_encontrado.apellido}")
    else:
        print("Cliente no encontrado")

def realizar_retiro(usuario):

    pass

def realizar_deposito(usuario):

    pass

def realizar_pago_tarjeta(usuario):
    pass

def realizar_pago_servicios(usuario):
    pass

def consultar_saldo(usuario):
    pass

def consultar_movimientos(usuario):
    pass

def main():
    usuario = iniciar_sesion()
    if usuario is None:
        print("Error al iniciar sesión. Inténtalo nuevamente.")
        return

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            realizar_retiro(usuario)
        elif opcion == '2':
            realizar_deposito(usuario)
        elif opcion == '3':
            realizar_pago_tarjeta(usuario)
        elif opcion == '4':
            realizar_pago_servicios(usuario)
        elif opcion == '5':
            consultar_saldo(usuario)
        elif opcion == '6':
            consultar_movimientos(usuario)
        elif opcion == '7':
            print("Sesión finalizada. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo nuevamente.")

if __name__ == "__main__":
    main()
