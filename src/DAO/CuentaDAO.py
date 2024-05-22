"""
DAO = Data Access Object.
Es un componente de software que suministra una interfaz común entre la aplicación y
uno o más dispositivos de almacenamiento de datos, tales como una Base de datos o 
un archivo.

Básicamente tenemos dos clases:
    1.  Cuenta.py - Creación del objeto
    2.  CuentaDAO.py - Conversión del objeto en una consulta a la base de datos
        (Definidas debajo).
"""

from db_management.logger_base import *
from function_modules.Cuenta import *
from db_management.Conexion import *
from db_management.cursor_del_pool import *

class CuentaDAO:
    _SELECCIONAR = 'SELECT * FROM cuenta ORDER BY num_cuenta'
    _INSERTAR = 'INSERT INTO cuenta(num_cuenta, num_debito, saldo, vencimiento, nip) VALUES(%s, %s, %s, %s, %s)'
    _ACTUALIZAR = 'UPDATE cliente SET num_cuenta = %s, num_debito = %s, saldo = %s, vencimiento = %s, nip = %s WHERE  = %s, %s, %s, %s, %s'
    _BORRAR = 'DELETE FROM cuenta WHERE num_cuenta = %s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            cuentas = []
            for registro in registros:
                cuenta = Cuenta(registro[0], registro[1], registro[2], registro[3], registro[4])
                cuentas.append(cuenta)
            return cuentas
        
    @classmethod
    def insertar(cls, cuenta):
        with CursorDelPool() as cursor:
            valores = (cuenta.num_cuenta, cuenta.num_debito, cuenta.saldo, cuenta.vencimiento, cuenta.nip)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Registro insertado en la base de datos: {cuenta}')
            return cursor.rowcount
        
    @classmethod
    def actualizar(cls, cuenta):
        with CursorDelPool() as cursor:
            valores = (cuenta.num_cuenta, cuenta.num_debito, cuenta.saldo, cuenta.vencimiento, cuenta.nip)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Registro actualizado: {cuenta}')
            return cursor.rowcount

    @classmethod
    def borrar(cls, cuenta):
        with CursorDelPool() as cursor:
            valores = (cuenta.num_cuenta)
            cursor.execute(cls._BORRAR, valores)
            log.debug(f'Registro eliminado: {cuenta}')
            return cursor.rowcount

if __name__ == '__main__':
    # Insertar un registro
    cuenta1 = Cuenta('1234567890', '1234353546', '3456', '03/30', '1234')
    cuentas_insertadas = CuentaDAO.insertar(cuenta1)
    log.debug(f'Registro insertado en la base de datos: {cuentas_insertadas}')

    # Seleccionar objetos
    cuentas = CuentaDAO.seleccionar()
    for cuenta in cuentas:
        log.debug(cuenta)
