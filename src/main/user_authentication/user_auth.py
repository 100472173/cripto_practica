from database_management import db_management
import re
def check_username_syntax(username: str):
    """ Comprueba que el nombre de usuario sigue el patrón definido como correcto
        El patrón sigue estas reglas:
        - Debe contener al menos una letra
        - La longitud debe estar entre 4-20 caracteres
        """
    validation_pattern = r"^(?=.*[a-zA-Z]).{4,20}$"
    my_regex = re.compile(validation_pattern)
    result = my_regex.fullmatch(username)
    if not result:
        print("Wrong pattern")
    else:
        print("OK.")

def check_pwd_syntax(pwd: str):
    """Comprueba que la contraseña sigue el patrón definido como correcto
           El patrón sigue estas reglas:
              - Al menos una mayúscula
              - Al menos un número
              - Al menos un caracter especial (~@_/+:)
              - Longitud de al menos 8 caracteres"""



