import sys
from CajeroDAO import *
from logger_base import *
from cifrado import *


class Cajero:
    def __init__(self, id_cajero = None, saldo  = None):
        self._id_cajero = id_cajero
        self._saldo = saldo


    def __str__(self):
        return  f'''
                Cajero: {self._id_cajero}
                Saldo: {self._saldo}
                '''
    
    @property
    def id_cajero(self):
        return self._id_cajero
    
    @id_cajero.setter
    def id_cajero(self, id_cajero):
        self._id_cajero = id_cajero

    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo
    
    
if __name__ == '__main__':
    cajero1 = Cajero(1, 50000)
    log.debug(cajero1)

    cajero2 = Cajero(11, 34875.65)
    CajeroDAO.insertar(cajero2)
    log.debug(cajero2)