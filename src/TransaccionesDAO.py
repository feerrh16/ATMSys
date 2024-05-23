"""
DAO = Data Access Object.
Es un componente de software que suministra una interfaz común entre la aplicación y
uno o más dispositivos de almacenamiento de datos, tales como una Base de datos o 
un archivo.

Básicamente tenemos dos clases:
    1.  Transacciones.py - Creación del objeto
    2.  TransaccionesDAO.py - Conversión del objeto en una consulta a la base de datos
        (Definidas debajo).
"""

import sys

from Cliente import *
from logger_base import *
from Transacciones import Movimiento, Cuenta
from Conexion import *
from cursor_del_pool import *


class TransaccionesDAO:
    # Métodos anteriores...

    @classmethod
    def seleccionar_por_numero(cls, num_debito):
        with CursorDelPool() as cursor:
            query = 'SELECT * FROM transacciones WHERE num_debito = %s'
            cursor.execute(query, (num_debito,))
            registro = cursor.fetchone()
            if registro:
                return Cuenta(registro[0], registro[1], registro[2], registro[3], registro[4])
            else:
                return None

    @classmethod
    def seleccionar_movimientos_por_cuenta(cls, num_debito):
        with CursorDelPool() as cursor:
            query = 'SELECT * FROM movimientos WHERE num_debito = %s ORDER BY fecha DESC'
            cursor.execute(query, (num_debito,))
            registros = cursor.fetchall()
            movimientos = []
            for registro in registros:
                movimiento = Movimiento(registro[0], registro[1], registro[2], registro[3], registro[4])
                movimientos.append(movimiento)
            return movimientos


class ClienteDAO:
    _SELECCIONAR = 'SELECT * FROM transacciones ORDER BY id_transaccion'
    _INSERTAR = 'INSERT INTO cliente(nombre, apellido) VALUES(%s, %s)'
    _ACTUALIZAR = 'UPDATE cliente SET nombre = %s, apellido = %s WHERE id_persona = %s'
    _BORRAR = 'DELETE FROM persona WHERE id_persona = %s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            clientes = []
            for registro in registros:
                cliente = Cliente(registro[0], registro[1], registro[2])
                clientes.append(cliente)
            return clientes
        
    @classmethod
    def insertar(cls, cliente):
        with CursorDelPool() as cursor:
            valores = (cliente.nombre, cliente.apellido)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Registro insertado en la base de datos: {cliente}')
            return cursor.rowcount
        
    @classmethod
    def actualizar(cls, cliente):
        with CursorDelPool() as cursor:
            valores = (cliente.nombre, cliente.apellido, cliente.id_cliente)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Registro actualizado: {cliente}')
            return cursor.rowcount

    @classmethod
    def borrar(cls, cliente):
        with CursorDelPool() as cursor:
            valores = (cliente.id_cliente)
            cursor.execute(cls._BORRAR, valores)
            log.debug(f'Registro eliminado: {cliente}')
            return cursor.rowcount

    @classmethod
    def seleccionar_por_numero(cls, num_debito):
        with CursorDelPool() as cursor:
            query = 'SELECT * FROM transacciones WHERE num_debito = %s'
            cursor.execute(query, (num_debito,))
            registro = cursor.fetchone()
            if registro:
                return Cuenta(registro[0], registro[1], registro[2], registro[3], registro[4])
            else:
                return None

    @classmethod
    def seleccionar_movimientos_por_cuenta(cls, num_debito):
        with CursorDelPool() as cursor:
            query = 'SELECT * FROM movimientos WHERE num_debito = %s ORDER BY fecha DESC'
            cursor.execute(query, (num_debito,))
            registros = cursor.fetchall()
            movimientos = []
            for registro in registros:
                movimiento = Movimiento(registro[0], registro[1], registro[2], registro[3], registro[4])
                movimientos.append(movimiento)
            return movimientos


if __name__ == '__main__':
    # Insertar un registro
    cliente1 = Cliente(nombre = 'Alejandra', apellido = 'Téllez')
    clientes_insertados = ClienteDAO.insertar(cliente1)
    log.debug(f'Registro insertado en la base de datos: {clientes_insertados}')

    # Seleccionar objetos
    clientes = ClienteDAO.seleccionar()
    for cliente in clientes:
        log.debug(cliente)
