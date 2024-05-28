"""
DAO = Data Access Object.
Es un componente de software que suministra una interfaz común entre la aplicación y
uno o más dispositivos de almacenamiento de datos, tales como una Base de datos o 
un archivo.

Básicamente tenemos dos clases:
    1.  TDC.py - Creación del objeto
    2.  TDCDAO.py - Conversión del objeto en una consulta a la base de datos
        (Definidas debajo).
"""

from logger_base import *
from Conexion import *
from cursor_del_pool import *

class TDCDAO:
    _SELECCIONAR = 'SELECT * FROM tarjeta_cto ORDER BY num_tarjeta'
    _INSERTAR = 'INSERT INTO tarjeta_cto(num_tarjeta, num_cuenta, nip, saldo_actual, a_pagar, fecha_vencimiento) VALUES(%s, %s, %s, %s, %s, %s)'
    _ACTUALIZAR = 'UPDATE tarjeta_cto SET num_tarjeta = %s, num_cuenta = %s, nip = %s, saldfacebook.como_actual = %s, a_pagar = %s, fecha_vencimiento = %s WHERE num_tarjeta = %s'
    _BORRAR = 'DELETE FROM tarjeta_cto WHERE num_tarjeta = %s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            tarjetas = []
            for registro in registros:
                tarjeta_cto = TDC(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5])
                tarjetas.append(tarjeta_cto)
            return tarjetas
        
    @classmethod
    def insertar(cls, tarjeta_cto):
        with CursorDelPool() as cursor:
            valores = (tarjeta_cto.num_tarjeta, tarjeta_cto.num_cuenta, tarjeta_cto.nip, tarjeta_cto.saldo_actual, tarjeta_cto.a_pagar, tarjeta_cto.fecha_vencimiento)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Registro insertado en la base de datos: {tarjeta_cto}')
            return cursor.rowcount
        
    @classmethod
    def actualizar(cls, tarjeta_cto):
        with CursorDelPool() as cursor:
            valores = (tarjeta_cto.num_cuenta, tarjeta_cto.num_cuenta, tarjeta_cto.nip, tarjeta_cto.saldo_actual, tarjeta_cto.a_pagar, tarjeta_cto.fecha_vencimiento)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Registro actualizado: {tarjeta_cto}')
            return cursor.rowcount

    @classmethod
    def borrar(cls, tarjeta_cto):
        with CursorDelPool() as cursor:
            valores = (tarjeta_cto.num_tarjeta)
            cursor.execute(cls._BORRAR, valores)
            log.debug(f'Registro eliminado: {tarjeta_cto}')
            return cursor.rowcount
        
# Módulo de pruebas para el módulo.
if __name__ == '__main__':
    # Insertar un registro
    from TDC import TDC
    tdc1 = TDC(11, 11, 5678, 5400, 160000, "12/06/24")
    tarjetas_insertadas = TDCDAO.insertar(tdc1)
    log.debug(f'Registro insertado en la base de datos: {tarjetas_insertadas}')

    # Seleccionar objetos
    tarjetas = TDCDAO.seleccionar()
    for tarjeta_cto in tarjetas:
        log.debug(tarjeta_cto)
