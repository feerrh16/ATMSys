import hashlib

def cifrar_datos(datos):
    hash_object = hashlib.sha512(datos.encode())
    return hash_object.hexdigest()

'''
Este modulo cifra cualquier tipo de datos por el metodo SHA512 que es el que acordamos en clase.
Asi que cuakquier cosa que quieras cifrar esta funcion lo retorna como un hash_object() o un objeto cifrado.
Es util ya que puedes cifrar datos en cualquier momento y en cualquier parte del codigo independientemente de la BD,
ya que puedes guardar esos datos cifrados antes de guardarlos en la BD o como te acomodes
'''
