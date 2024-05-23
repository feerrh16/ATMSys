"""
DAO = Data Access Object.
Es un componente de software que suministra una interfaz común entre la aplicación y
uno o más dispositivos de almacenamiento de datos, tales como una Base de datos o 
un archivo.

Básicamente tenemos dos clases:
    1.  PagoServicios.py - Creación del objeto
    2.  PagoServiciosDAO.py - Conversión del objeto en una consulta a la base de datos
        (Definidas debajo).
"""

import sys
from logger_base import *
from PagoServicios import PagoServicios
from Conexion import *
from cursor_del_pool import *

class PagoServiciosDAO:
    _SELECCIONAR = 'SELECT * FROM pago_servicio ORDER BY id_pago'
    _INSERTAR = 'INSERT INTO pago_servicio(id_pago, id_servicio, num_cuenta, monto) VALUES(%s, %s, %s, %s)'
    _ACTUALIZAR = 'UPDATE pago_servicio SET id_pago = %s, id_servicio = %s, num_cuenta = %s, monto = %s WHERE id_pago = %s'
    _BORRAR = 'DELETE FROM pago_servicio WHERE id_pago = %s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            pagos = []
            for registro in registros:
                pago_servicio = PagoServicios(registro[0], registro[1], registro[2], registro[3])
                pagos.append(pago_servicio)
            return pagos
        
    @classmethod
    def insertar(cls, pago_servicio):
        with CursorDelPool() as cursor:
            valores = (pago_servicio.id_pago, pago_servicio.id_servicio, pago_servicio.num_cuenta, pago_servicio.monto)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Registro insertado en la base de datos: {pago_servicio}')
            return cursor.rowcount
        
    @classmethod
    def actualizar(cls, pago_servicio):
        with CursorDelPool() as cursor:
            valores = (pago_servicio.id_pago, pago_servicio.id_servicio, pago_servicio.num_cuenta, pago_servicio.monto)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Registro actualizado: {pago_servicio}')
            return cursor.rowcount

    @classmethod
    def borrar(cls, pago_servicio):
        with CursorDelPool() as cursor:
            valores = (pago_servicio.id_pago)
            cursor.execute(cls._BORRAR, valores)
            log.debug(f'Registro eliminado: {pago_servicio}')
            return cursor.rowcount
        
# Módulo de pruebas para el módulo.
if __name__ == '__main__':
    # Insertar un registro
    pago1 = PagoServicios(11, "Gas", 1, 150)
    pagos_insertados = PagoServiciosDAO.insertar(pago1)
    log.debug(f'Registro insertado en la base de datos: {pagos_insertados}')

    # Seleccionar objetos
    pagos = PagoServiciosDAO.seleccionar()
    for pago_servicio in pagos:
        log.debug(pago_servicio)
