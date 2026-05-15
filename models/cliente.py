from exceptions.custom_exceptions import ClienteInvalidoError

class Cliente:
    def __init__(self, nombre, documento, email):
        # Validaciones para el cliente        
        if not nombre.strip(): 
            raise ClienteInvalidoError("El nombre del cliente no puede estar vacío") 
        
        if "@" not in email or "." not in email:
            raise ClienteInvalidoError("El email del cliente no es válido")
        
        if not documento.strip():
            raise ClienteInvalidoError("El documento del cliente no puede estar vacío")
        
        self.__nombre = nombre
        self.__documento = documento
        self.__email = email

    def mostrar_info(self):
        return f"{self.__nombre}\nDocumento: {self.__documento} Email: {self.__email}"