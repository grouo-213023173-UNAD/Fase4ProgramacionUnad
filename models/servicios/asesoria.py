from models.servicio import Servicio

class Asesoria(Servicio):

    def __init__(self, nombre, costo_base, horas):
        super().__init__(nombre, costo_base)
        self.horas = horas
    
    def calcular_costo(self):
        return round(self._costo_base * self.horas * 1.15)
    
    def mostrar_descripcion(self):
        return f"{self._nombre}\nHoras de asesoría: {self.horas}\nCosto total: ${self.calcular_costo()}"