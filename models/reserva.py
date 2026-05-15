from exceptions.custom_exceptions import ReservaError       

class Reserva:
    def __init__(self, cliente, servicio, duracion):

        if duracion <= 0:
            raise ReservaError("La duración de la reserva debe ser mayor a cero")
        
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar_reserva(self):

        self.estado = "Confirmada"
        return "Resrva confirmada correctamente"
    
    def cancelar_reserva(self):

        self.estado = "Cancelada"
        return "Reserva cancelada correctamente"
    
    def mostrar_reserva(self):
        return f"Cliente: {self.cliente.mostrar_info()}\nServicio: {self.servicio.mostrar_descripcion()}\nDuración: {self.duracion} horas\nEstado: {self.estado}"