from cryptography.hazmat.primitives.asymmetric import rsa
import os
def write_file(username, key1: bytes):
    try:
        directorio_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_absoluta = os.path.join(directorio_actual, '..', 'user_files', "files.txt")
        with open(ruta_absoluta, 'a') as archivo:
            archivo.write(f"{username}:{key1};\n")
        print(f"Se ha escrito en el archivo: {ruta_absoluta}")
    except Exception as e:
        print(f"Error al escribir en el archivo: {e}")

def generate_key(user):
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    write_file(user, private_key)

def signing(mensaje, user):
    mensaje_bytes = mensaje.encode('utf-8')
    private_key = read_file(user)
    signature = private_key.sign(
        message_bytes,
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
            message_bytes,
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