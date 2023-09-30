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
        print("OK")


def check_pwd_syntax(pwd: str):
    validation_pattern = r"^(?=.*[A-Z])(?=.*\d)(?=.*[!~@_/:+]).{8,}$"
    my_regex = re.compile(validation_pattern)
    result = my_regex.fullmatch(pwd)
    if not result:
        print("Wrong pattern")
    else:
        print("OK.")


