from models.servicio import Servicio

class AlquilerEquipo(Servicio):

    def __init__(self, nombre, costo_base, dias):
        super().__init__(nombre, costo_base)
        self.dias = dias
    
    def calcular_costo(self):
        return round(self._costo_base * self.dias)
    
    def mostrar_descripcion(self):
        return f"{self._nombre}\nDías de alquiler: {self.dias}\nCosto: ${self.calcular_costo()}"