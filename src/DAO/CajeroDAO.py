"""
DAO = Data Access Object.
Es un componente de software que suministra una interfaz común entre la aplicación y
uno o más dispositivos de almacenamiento de datos, tales como una Base de datos o 
un archivo.

Básicamente tenemos dos clases:
    1.  Cajero.py - Creación del objeto
    2.  CajeroDAO.py - Conversión del objeto en una consulta a la base de datos
        (Definidas debajo).
"""

from logger_base import *
from Cajero import *
from Conexion import *
from cursor_del_pool import *

class CajeroDAO:
    _SELECCIONAR = 'SELECT * FROM cajero ORDER BY id_cajero'
    _INSERTAR = 'INSERT INTO cajero(id_cajero, saldo) VALUES(%s, %s)'
    _ACTUALIZAR = 'UPDATE cajero SET id_cajero = %s, saldo = %s WHERE id_cajero = %s'
    _BORRAR = 'DELETE FROM cajero WHERE id_cajero = %s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            cajeros = []
            for registro in registros:
                cajero = Cajero(registro[0], registro[1], registro[2])
                cajeros.append(cajero)
            return cajeros
        
    @classmethod
    def insertar(cls, cajero):
        with CursorDelPool() as cursor:
            valores = (cajero.id_cajero, cajero.saldo)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Registro insertado en la base de datos: {cajero}')
            return cursor.rowcount
        
    @classmethod
    def actualizar(cls, cajero):
        with CursorDelPool() as cursor:
            valores = (cajero.id_cajero, cajero.saldo)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Registro actualizado: {cajero}')
            return cursor.rowcount

    @classmethod
    def borrar(cls, cajero):
        with CursorDelPool() as cursor:
            valores = (cajero.id_cajeroCajero)
            cursor.execute(cls._BORRAR, valores)
            log.debug(f'Registro eliminado: {cajero}')
            return cursor.rowcount
        
# Módulo de pruebas para el módulo.
if __name__ == '__main__':
    # Insertar un registro
    cajero1 = Cajero(id_cajero = 11, saldo = 43765.98)
    cajeros_insertados = CajeroDAO.insertar(cajero1)
    log.debug(f'Registro insertado en la base de datos: {cajeros_insertados}')

    # Seleccionar objetos
    cajeros = CajeroDAO.seleccionar()
    for cajero in cajeros:
        log.debug(cajero)
