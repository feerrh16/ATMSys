from db_management.logger_base import *

class Cuenta:
    def __init__(self, ID_Transaccion = None, num_debito = None, saldo = None, vencimiento = None, nip = None):
        self._id_transaccion = ID_Transaccion
        self._num_debito = num_debito
        self._saldo = saldo
        self._vencimiento = vencimiento
        self._nip = nip

    def __str__(self):
        return  f'''
                Número de cuenta: {self._num_cuenta}
                Tarjeta número: {self._num_debito}
                Vencimiento: {self._vencimiento}
                Saldo disponible= {self._saldo}
                '''
    
    @property
    def vencimiento(self):
        return self._vencimiento
    
    @vencimiento.setter
    def vencimiento_cuenta(self, vencimiento):
        self._vencimiento = vencimiento

    @property
    def nip(self):
        return self.nip
    
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
    def num_debito(self):
        return self._num_debito
    
    @num_debito.setter
    def num_debito(self, num_debito):
        self._num_debito = num_debito
    
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, saldo):
        self._saldo
    
if __name__ == '__main__':
    cliente1 = Cuenta('1111-1111-1111-1111', '2345-5467-1234-2436', '2500', '05/30', '1212')
    log.debug(cliente1)

