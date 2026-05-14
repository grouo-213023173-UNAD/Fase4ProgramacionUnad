from exceptions.custom_exceptions import ClienteInvalidoError


try:

    raise ClienteInvalidoError("El cliente no tiene un email válido")

except ClienteInvalidoError as error:

    print(f"Error detectado: {error}")