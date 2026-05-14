from models.cliente import Cliente
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