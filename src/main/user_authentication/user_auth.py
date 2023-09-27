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

"""
mirar en cryptography.io
Hay que guardar en la tabla usuarios el usuario, la contraseña en forma de token y el salt


hay que a parte de derivar la password en un token, verificarla
def generate_pwd_token(pwd: str):
    salt = os.urandom(16)
    kdf = Scrypt (
        salt = salt,
        length = 32,
        n =2**14,
        r=8,
        p=1)        
    pwd_token = kdf.derive(b(pwd))
    return pwd_token"""
