from models.servicio import Servicio

class ReservaSala(Servicio):
    
    def __init__(self, nombre, costo_base, capacidad):
        super().__init__(nombre, costo_base)
        self.capacidad = capacidad

    def calcular_costo(self):
        return round(self._costo_base * 1.10)
    
    def mostrar_descripcion(self):
        return f"Servicio: {self._nombre}\nCapacidad: {self.capacidad} personas\nCosto: ${self.calcular_costo()}"