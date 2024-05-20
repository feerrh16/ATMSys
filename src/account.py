# account.py
from db import execute_query, fetch_query

def check_balance(num_cuenta):
    query = "SELECT saldo FROM cuenta WHERE num_cuenta = %s"
    result = fetch_query(query, (num_cuenta,))
    if result:
        return result[0][0]
    return None

def deposit(num_cuenta, amount):
    query = "UPDATE cuenta SET saldo = saldo + %s WHERE num_cuenta = %s"
    execute_query(query, (amount, num_cuenta))
    register_transaction(num_cuenta, 1, 'Depósito de {}'.format(amount))

def withdraw(num_cuenta, amount):
    current_balance = check_balance(num_cuenta)
    if current_balance is not None and current_balance >= amount:
        query = "UPDATE cuenta SET saldo = saldo - %s WHERE num_cuenta = %s"
        execute_query(query, (amount, num_cuenta))
        register_transaction(num_cuenta, 2, 'Retiro de {}'.format(amount))
    else:
        raise Exception("Fondos insuficientes")

def transfer(from_account, to_account, amount):
    withdraw(from_account, amount)
    deposit(to_account, amount)
    register_transaction(from_account, 3, 'Transferencia a {} de {}'.format(to_account, amount))
    register_transaction(to_account, 3, 'Transferencia recibida de {} de {}'.format(from_account, amount))

def register_transaction(num_cuenta, id_tipoMovimiento, concepto):
    query = """
    INSERT INTO transacciones (num_cuenta, id_cajero, id_tipoMovimiento, fecha_movimiento, concepto)
    VALUES (%s, %s, %s, NOW(), %s)
    """
    execute_query(query, (num_cuenta, None, id_tipoMovimiento, concepto))
