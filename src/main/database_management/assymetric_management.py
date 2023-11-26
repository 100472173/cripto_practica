from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography import x509
from cryptography.x509.oid import NameOID

import os


def generate_key(user):
    """Funcion encargada de generar una clave publica para un usuario"""
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    # Se guarda la la clave en un fichero especifico al usuario (ya se vera que antes se ha de serializar)
    save_to_file(user, private_key)
    return private_key


def certificate_request(user, key):
    csr = x509.CertificateSigningRequestBuilder().subject_name(x509.Name([
        # Provide various details about who we are.
        x509.NameAttribute(NameOID.COUNTRY_NAME, "US"),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "California"),
        x509.NameAttribute(NameOID.LOCALITY_NAME, "San Francisco"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, "My Company"),
        x509.NameAttribute(NameOID.COMMON_NAME, "mysite.com"),
    ])).add_extension(
        x509.SubjectAlternativeName([
            # Describe what sites we want this certificate for.
            x509.DNSName("mysite.com"),
            x509.DNSName("www.mysite.com"),
            x509.DNSName("subdomain.mysite.com"),
        ]),
        critical=False,
        # Sign the CSR with our private key.
    ).sign(key, hashes.SHA256())
    with open("path/to/csr.pem", "wb") as f:
        f.write(csr.public_bytes(serialization.Encoding.PEM))


def serialize(private_key):
    """Funcion que serializa una clave privada para poder guardarla en un fichero de salida asociado al usuario"""
    pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.BestAvailableEncryption(b'yeah_ivan')
    )
    return pem


def save_to_file(username, private_key):
    """Funcion encargada de guardar en un fichero asociado al usuario su clave privada serializada"""
    try:
        # Se crea un fichero de tipo username_key.pem
        directorio_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_absoluta = os.path.join(directorio_actual, '..', 'user_files')
        file_path = os.path.join(ruta_absoluta, f"{username}_key.pem")
        # Se serializa la clave privada
        pem = serialize(private_key)
        # Escritura en el archivo de la clave serializada
        with open(file_path, 'wb') as file:
            file.write(pem)
        print(f"Se ha guardado la clave para el usuario '{username}' en el archivo: {file_path}")
    # Captura de cualquier excepcion mediante depuracion por terminal
    except Exception as e:
        print(f"Error al guardar en el archivo: {e}")


def signing(mensaje, user):
    """Funcion que lleva a cabo el proceso de firma por el mensaje de la accion realizada por el usuario"""
    mensaje_bytes = mensaje.encode('utf-8')
    # Se lee la clave deserializada
    private_key = read_file(user)
    # Proceso de firma
    signature = private_key.sign(
        mensaje_bytes,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature


def verify(user, signature, mensaje):
    # Obtencion de la clave publica
    public_key = read_file(user)
    mensaje_bytes = mensaje.encode('utf-8')
    # Se intenta verificar la firma a traves de la clave publica mediante trata de excepciones
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
    except InvalidSignature as e:
        raise e


def read_file(username):
    """Funcion encargada de leer un fichero que alberga una clave privada, y deserializarla"""
    try:
        directorio_actual = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(directorio_actual, '..', 'user_files', f"{username}_key.pem")

        if not os.path.exists(file_path):
            print(f"El archivo para el usuario '{username}' no existe.")
            return None

        with open(file_path, 'rb') as file:
            pem_content = file.read()
        # Si ha ido bien, se deserializa y devuelve el contenido de la clave privada
        print(f"Se ha leído el contenido del archivo para el usuario '{username}'.")
        content = deserialize(pem_content)
        return content
    # Trata de excepciones
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None


def deserialize(data):
    """Funcion que lleva a cabo la tarea de deserializar una clave 'data' junto a su password asociado"""
    private_key = serialization.load_pem_private_key(
        data,
        password=b'yeah_ivan',
        backend=default_backend()
    )
    return private_key


if __name__ == "__main__":
    generate_key("Tomas")
    signing("Hola wachos", "Tomas")
