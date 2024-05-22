from user import *
from account import check_balance, deposit, withdraw, transfer

def main():
    print("Bienvenido al cajero automático")
    id_cliente = int(input("Ingrese su ID de cliente: "))
    user = login(id_cliente)
    if user:
        print("Bienvenido, {} {}".format(user[1], user[2]))
        num_cuenta = int(input("Ingrese su número de cuenta: "))
        
        while True:
            print("\nElija una opción:")
            print("1. Consultar saldo")
            print("2. Depositar")
            print("3. Retirar")
            print("4. Transferir")
            print("5. Salir")
            opcion = input("Ingrese el número de la opción: ")
            
            if opcion == '1':
                balance = check_balance(num_cuenta)
                print("Su saldo es: {:.2f}".format(balance))
            
            elif opcion == '2':
                amount = float(input("Ingrese el monto a depositar: "))
                deposit(num_cuenta, amount)
                print("Depósito exitoso.")
            
            elif opcion == '3':
                amount = float(input("Ingrese el monto a retirar: "))
                try:
                    withdraw(num_cuenta, amount)
                    print("Retiro exitoso.")
                except Exception as e:
                    print(e)
            
            elif opcion == '4':
                to_account = int(input("Ingrese el número de cuenta destino: "))
                amount = float(input("Ingrese el monto a transferir: "))
                try:
                    transfer(num_cuenta, to_account, amount)
                    print("Transferencia exitosa.")
                except Exception as e:
                    print(e)
            
            elif opcion == '5':
                print("Gracias por usar el cajero automático.")
                break
            
            else:
                print("Opción no válida. Intente nuevamente.")
    else:
        print("ID de cliente no encontrado. Intente nuevamente.")

if __name__ == "__main__":
    main()
