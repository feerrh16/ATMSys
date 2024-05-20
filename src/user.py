# user.py
from db import fetch_query

def login(id_cliente):
    query = "SELECT id_cliente, nombre, apellido FROM cliente WHERE id_cliente = %s"
    result = fetch_query(query, (id_cliente,))
    if result:
        return result[0]
    return None
