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
        print(username)
        return False
    return True


def check_pwd_syntax(pwd: str):
    validation_pattern = r"^(?=.*[A-Z])(?=.*\d)(?=.*[!~@_/:+]).{8,}$"
    my_regex = re.compile(validation_pattern)
    result = my_regex.fullmatch(pwd)
    if not result:
        print(pwd)
        return False
    return True


def check_names_syntax(name: str):
    validation_pattern = r"^[A-Z][a-zA-Z]{0,19}$"
    my_regex = re.compile(validation_pattern)
    result = my_regex.fullmatch(name)
    if not result:
        print(name)
        return False
    return True


def check_email_syntax(email: str):
    validation_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    my_regex = re.compile(validation_pattern)
    result = my_regex.fullmatch(email)
    if not result:
        print(email)
        return False
    return True


def check_money(money: str):
    if not money.isdigit():
        print(money)
        return False
    if len(money) > 7:
        print(money)
        return False
    return True
