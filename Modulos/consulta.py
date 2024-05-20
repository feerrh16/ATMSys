def consultar_saldo_movimientos(usuario):
    print("Consulta de saldos y movimientos")
    # Aquí se debería obtener el saldo y los movimientos de la base de datos
    saldo = 1000  # Valor de ejemplo
    movimientos = [
        {"fecha": "2024-01-01", "concepto": "Depósito", "acreedor": "Banco", "cantidad": 500},
        {"fecha": "2024-01-02", "concepto": "Retiro", "acreedor": "Cajero", "cantidad": 200},
        # Agregar más movimientos de ejemplo
    ]
    print(f"Saldo actual: ${saldo}")
    print("Últimos movimientos:")
    for mov in movimientos[:5]:
        print(f"{mov['fecha']} - {mov['concepto']} - {mov['acreedor']} - ${mov['cantidad']}")

# Aqui se agrega la logica de la BD
