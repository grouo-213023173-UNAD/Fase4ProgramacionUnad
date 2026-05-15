from models.cliente import Cliente
from models.servicio import Servicio
from models.reserva import Reserva
from exceptions.custom_exceptions import ReservaError
from models.servicios.reserva_sala import ReservaSala
from exceptions.custom_exceptions import ClienteInvalidoError


try:

    cliente1 = Cliente(
        "Daniel",
        "123456",
        "daniel@gmail.com"
    )

    print(cliente1.mostrar_info())

except ClienteInvalidoError as error:

    print(f"Error: {error}")

sala = ReservaSala(
    "Sala premium",
    200,
    20
)

try:
    reserva1 = Reserva(
        cliente1,
        sala,
        3
    )

    print(reserva1.mostrar_reserva())
    print(reserva1.confirmar_reserva())
    print(reserva1.mostrar_reserva())

except ReservaError as error:
        print(f"Error en reserva: {error}")