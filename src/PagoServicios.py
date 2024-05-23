import sys
from PagoServiciosDAO import *
from logger_base import *
from cifrado import *

class PagoServicios:
    def __init__(self, id_pago = None, id_servicio = None, num_cuenta = None, monto = None):
        self._id_pago = id_pago
        self._id_servicio = id_servicio
        self._num_cuenta = num_cuenta
        self.monto = monto

    def __str__(self):
        return  f'''
                ID: {self._id_pago}
                Servicio: {self._id_servicio}
                Cuenta = {self._num_cuenta}
                Monto = {self._monto}
                '''
    
    @property
    def id_pago(self):
        return self._id_pago
    
    @id_pago.setter
    def id_pago(self, id_pago):
        self._id_pago = id_pago

    @property
    def id_servicio(self):
        return self._id_servicio
    
    @id_servicio.setter
    def id_servicio(self, id_servicio):
        self._id_servicio = id_servicio
    
    @property
    def num_cuenta(self):
        return self._num_cuenta
    
    @num_cuenta.setter
    def num_cuenta(self, num_cuenta):
        self._num_cuenta = num_cuenta

    @property
    def monto(self):
        return self._monto
    
    @monto.setter
    def monto(self, monto):
        self._monto = monto
    
    
if __name__ == '__main__':
    pago1 = PagoServicios(5, "Gas", 4444444444444444, 399)
    log.debug(pago1)

    pago2 = PagoServicios(1, "Agua", 5555555555555555, 599)
    log.debug(pago2)