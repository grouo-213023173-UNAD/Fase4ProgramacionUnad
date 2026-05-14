 # Importamos la clase datetime del módulo datetime para trabajar con fechas y horas
from datetime import datetime
# Función para registrar un mensaje en el archivo de log
def registrar_log(mensaje):
    # Intentamos abrir el archivo de log en modo de adición ('a') para agregar el mensaje al final del archivo
    try: #
        with open('data/logs.txt', 'a', encoding='utf-8') as archivo:
            # Obtenemos la fecha y hora actual formateada como una cadena
            fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            archivo.write(f'[{fecha}]: {mensaje}\n')
    except Exception as error:
        # Si ocurre un error al intentar escribir en el archivo de log, se captura la excepción y se imprime un mensaje de error
        print(f'Error al registrar log: {error}')