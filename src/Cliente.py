import sys
sys.path.append('ATMSys-1/src/DAO')
sys.path.append('ATMSys-1/src/db_management')
sys.path.append('ATMSys-1/src/function_models')
sys.path.append('ATMSys-1/src/security')
from logger_base import *
from cifrado import *

class Cliente:
    def __init__(self, id_persona = None, nombre = None, apellido = None):
        self._id_persona = id_persona
        self._nombre = nombre
        self._apellido = apellido

    def __str__(self):
        return  f'''
                ID: {self._id_persona}
                Nombre: {self._nombre}
                Apellido = {self._apellido}
                '''
    
    @property
    def id_persona(self):
        return self._id_persona
    
    @id_persona.setter
    def id_persona(self, id_persona):
        self._id_persona = id_persona

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self, apellido):
        self._apellido
    
if __name__ == '__main__':
    cliente1 = Cliente(1, 'Juan', 'Pérez')
    log.debug(cliente1)

    cliente2 = Cliente(11, 'German', 'Sánchez')
    log.debug(cliente2)
