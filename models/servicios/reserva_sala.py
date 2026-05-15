from models.servicio import Servicio

class ReservaSala(Servicio):
    
    def __init__(self, nombre, costo_base, capacidad):
        super().__init__(nombre, costo_base)
        self.capacidad = capacidad

    def calcular_costo(self, impuesto=0, descuento=0):
        costo = self._costo_base
        costo += costo *impuesto
        costo -= costo * descuento
        return round(costo)
        
    
    def mostrar_descripcion(self):
        return f"{self._nombre}\nCapacidad: {self.capacidad} personas\nCosto: ${self.calcular_costo()}"