from Modulos import autenticar as auth
from Modulos import retiro
from Modulos import deposito
from Modulos import pago
from Modulos import servicios
from Modulos import consulta


def mostrar_menu_principal():
    print("Bienvenido al sistema de gestión financiera ATMSys")
    print("1. Retiro de efectivo")
    print("2. Depósito de efectivo")
    print("3. Pago de tarjeta de crédito")
    print("4. Pago de servicios")
    print("5. Consulta de saldos/movimientos")
    print("6. Salir")


def ejecutar_operacion(opcion, usuario):
    if opcion == 1:
        retiro.retirar_efectivo(usuario)
    elif opcion == 2:
        deposito.depositar_efectivo(usuario)
    elif opcion == 3:
        pago.pagar_tarjeta(usuario)
    elif opcion == 4:
        servicios.pagar_servicio(usuario)
    elif opcion == 5:
        consulta.consultar_saldo_movimientos(usuario)
    elif opcion == 6:
        print("Gracias por usar el sistema. ¡Hasta luego!")
        return False
    else:
        print("Opción no válida. Por favor, elija una opción del menú.")
    return True


def main():
    usuario = auth.iniciar_sesion()
    if usuario:
        while True:
            mostrar_menu_principal()
            try:
                opcion = int(input("Seleccione una opción: "))
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número.")
                continue
            if not ejecutar_operacion(opcion, usuario):
                break
    else:
        print("Autenticación fallida. Por favor, inténtelo de nuevo.")


if __name__ == "__main__":
    main()
