from models.cliente import Cliente
from models.reserva import Reserva
from models.servicios.alquiler_equipo import AlquilerEquipo
from models.servicios.asesoria import Asesoria
from models.servicios.reserva_sala import ReservaSala

from exceptions.custom_exceptions import (
    ClienteInvalidoError,
    ReservaError
)

from utils.logger import registrar_log


print("\n--- INICIO DEL SISTEMA ---\n")


# OPERACIÓN 1
try:

    cliente1 = Cliente(
        "Daniel",
        "123456",
        "daniel@gmail.com"
    )

    registrar_log("Cliente Daniel registrado correctamente")

    print(f"{cliente1.mostrar_info()}\n")

except ClienteInvalidoError as error:

    registrar_log(f"Error cliente: {error}\n")

    print(error)


# OPERACIÓN 2
try:

    cliente2 = Cliente(
        "",
        "999999",
        "correo_malo"
    )

    print(f"{cliente2.mostrar_info()}\n")

except ClienteInvalidoError as error:

    registrar_log(f"Error cliente inválido: {error}\n")

    print(f"ERROR: {error}")


# OPERACIÓN 3
try:

    sala = ReservaSala(
        "Sala Premium",
        200,
        20
    )

    registrar_log("Servicio Sala Premium creado")

    print(f"{sala.mostrar_descripcion()}\n")

except Exception as error:

    registrar_log(f"Error servicio: {error}")

    print(error)


# OPERACIÓN 4
try:

    reserva1 = Reserva(
        cliente1,
        sala,
        3
    )

    registrar_log("Reserva creada correctamente")

    print(f"{reserva1.mostrar_reserva()}\n")

except ReservaError as error:

    registrar_log(f"Error reserva: {error}\n")

    print(error)


# OPERACIÓN 5
try:

    reserva_invalida = Reserva(
        cliente1,
        sala,
        -5
    )

except ReservaError as error:

    registrar_log(f"Reserva inválida detectada: {error}")

    print(f"ERROR: {error}\n")


# OPERACIÓN 6
try:

    print(f"{reserva1.confirmar_reserva()}\n")

    registrar_log("Reserva confirmada")

except Exception as error:

    registrar_log(f"Error confirmando reserva: {error}")

    print(f"ERROR: {error}\n")


# OPERACIÓN 7
try:

    print(f"{reserva1.cancelar_reserva()}\n")

    registrar_log("Reserva cancelada")

except Exception as error:

    registrar_log(f"Error cancelando reserva: {error}")

    print(f"ERROR: {error}\n")


# OPERACIÓN 8
try:

    cliente3 = Cliente(
        "Maria",
        "",
        "maria@gmail.com"
    )

except ClienteInvalidoError as error:

    registrar_log(f"Cliente inválido: {error}")

    print(f"ERROR: {error}\n")


# OPERACIÓN 9
try:

    cliente4 = Cliente(
        "Carlos",
        "777777",
        "carlosgmail.com"
    )

except ClienteInvalidoError as error:

    registrar_log(f"Email inválido: {error}\n")

    print(f"ERROR: {error}\n")


# OPERACIÓN 10
try:

    sala2 = ReservaSala(
        "Sala Ejecutiva",
        500,
        50
    )

    print(f"{sala2.mostrar_descripcion()}\n")

    registrar_log("Sala Ejecutiva creada")

except Exception as error:

    registrar_log(f"Error sala ejecutiva: {error}")

    print(f"ERROR: {error}\n")


# OPERACIÓN 11
try:

    alquiler = AlquilerEquipo(
        "Alquiler Computadores",
        100,
        5
    )

    print(f"{alquiler.mostrar_descripcion()}\n")

    registrar_log("Servicio alquiler creado")

except Exception as error:

    registrar_log(f"Error alquiler: {error}")

    print(error)

#OPERACIÓN 12
try:

    asesoria = Asesoria(
        "Asesoría Python",
        80,
        4
    )

    print(f"{asesoria.mostrar_descripcion()}\n")

    registrar_log("Servicio asesoría creado")

except Exception as error:

    registrar_log(f"Error asesoría: {error}")

    print(error)

finally:

    print("\n--- FIN DEL SISTEMA ---\n")

    registrar_log("Sistema finalizado")