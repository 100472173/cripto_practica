from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.asymmetric import rsa
import os
import json


def load_data():
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_absoluta = os.path.join(directorio_actual, '..', 'user_files', "files.json")
    try:
        with open(ruta_absoluta, 'r') as archivo:
            datos = json.load(archivo)
        return datos
    except FileNotFoundError:
        return {}

def save_data(data):
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_absoluta = os.path.join(directorio_actual, '..', 'user_files', "files.json")
    with open(ruta_absoluta, 'w') as archivo:
        json.dump(data, archivo, indent=2)

def read_file(username):
    try:
        datos = load_data()
        if username in datos:
            key = datos[username]
            print(f"La clave para el usuario '{username}' es: {key}")
            return key
        else:
            print(f"No se encontró el usuario '{username}' en el archivo.")
            return None
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None

def write_file(username, new_key):
    try:
        datos = load_data()
        # Actualizar la clave para el usuario o agregar un nuevo usuario
        save_data(datos[username])
    except Exception as e:
        print(f"Error al escribir en el archivo: {e}")

def signing(mensaje, user):
    mensaje_bytes = mensaje.encode('utf-8')
    private_key = read_file(user)
    signature = private_key.sign(
        mensaje_bytes,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    public_key = private_key.public_key()
    try:
        public_key.verify(
            signature,
            mensaje_bytes,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
    except InvalidSignature:
        print("No se ha podido verificar la transaccion")
        return None
    print("Usuario: " + user + ". " + mensaje)

def generate_key(user):
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    write_file(user, private_key)