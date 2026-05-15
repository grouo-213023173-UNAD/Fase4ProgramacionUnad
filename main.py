from models.cliente import Cliente
from models.servicio import Servicio
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

print(sala.mostrar_descripcion())  