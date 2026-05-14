from datetime import datetime
def registrar_log(mensaje):
    try:
        with open('data/log.txt', 'a') as archivo:
            fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            archivo.write(f'[{fecha}]: {mensaje}\n')
    except Exception as error:
        print(f'Error al registrar log: {error}')