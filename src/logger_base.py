import logging as log

log.basicConfig(level=log.INFO, 
                format = '%(asctime)s: %(levelname)s\n[%(filename)s: %(lineno)s]\n%(message)s\n',
                datefmt = '%I:%M:%S %p',
                handlers = [
                    log.FileHandler('D:\\ATMSys\\src\\capa_datos.log'),
                    log.StreamHandler()
                ])

if __name__ == '__main__':
    log.debug('Mensaje a nivel debug')
    log.info('Mensaje a nivel info')
    log.warning('Mensaje a nivel warning')
    log.error('Mensaje a nivel error')
    log.critical('Mensaje a nivel crítico')
