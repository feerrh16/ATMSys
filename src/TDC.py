import sys
sys.path.append('ATMSys-1/src/DAO')
sys.path.append('ATMSys-1/src/db_management')
sys.path.append('ATMSys-1/src/function_models')
sys.path.append('ATMSys-1/src/security')
from logger_base import *
from cifrado import *

class TDC:
    def __init__(self, num_tarjeta = None, num_cuenta = None, nip  = None, saldo_actual = None, a_pagar = None, fecha_vencimiento = None):
        self._num_tarjeta = num_tarjeta
        self._nip = nip
        self._num_cuenta = num_cuenta
        self._saldo_atual = saldo_actual
        self._a_pagar = a_pagar
        self._fecha_venicimiento = fecha_vencimiento


    def __str__(self):
        return  f'''
                Tarjeta: {self._num_tarjeta}
                Nip: {self._nip}
                Cuenta = {self._num_cuenta}
                Saldo = {self._saldo_atual}
                Cantidad = {self._a_pagar}
                Fecha = {self._fecha_venicimiento}
                '''
    
    @property
    def num_tarjeta(self):
        return self._num_tarjeta
    
    @num_tarjeta.setter
    def num_tarjeta(self, num_tarjeta):
        self._num_tarjeta = num_tarjeta

    @property
    def nip(self):
        return self._nip
    
    @nip.setter
    def nip(self, nip):
        self._nip = nip
    
    @property
    def num_cuenta(self):
        return self._num_cuenta 
    
    @num_cuenta.setter
    def num_cuenta(self, num_cuenta):
        self._num_cuenta = num_cuenta

    @property
    def saldo_actual(self):
        return self._saldo_atual 
    
    @saldo_actual.setter
    def saldo_actual(self, saldo_actual):
        self._saldo_atual = saldo_actual

    @property
    def a_pagar(self):
        return self._a_pagar
    
    @a_pagar.setter
    def a_pagar(self, a_pagar):
        self._a_pagar = a_pagar

    @property
    def fecha_vencimiento(self):
        return self._fecha_venicimiento
    
    @fecha_vencimiento.setter
    def fecha_vencimiento(self, fecha_ventimiento):
        self._fecha_venicimiento = fecha_ventimiento
    
    
if __name__ == '__main__':
    tdc1 = TDC(2222333344445555, 1234, 1111111111111111, 1500, 3500, "12/06/24")
    log.debug(tdc1)

    tdc2 = TDC(1111666677778888, 5678, 2222222222222222, 200, 9800, "16/06/24")
    log.debug(tdc2)