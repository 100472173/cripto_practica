import shutil
import subprocess

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography import x509
from cryptography.x509.oid import NameOID

from cryptography.hazmat.primitives.serialization import load_pem_public_key
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
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_absoluta = os.path.join(directorio_actual, '..', 'A')
    file_path = os.path.join(ruta_absoluta, f"{user}_request.pem")
    csr = x509.CertificateSigningRequestBuilder().subject_name(x509.Name([
        # Provide various details about who we are.
        x509.NameAttribute(NameOID.COUNTRY_NAME, "US"),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "California"),
        x509.NameAttribute(NameOID.LOCALITY_NAME, "San Francisco"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, f"{user}-company"),
        x509.NameAttribute(NameOID.COMMON_NAME, f"{user}mysite.com"),
    ])).add_extension(
        x509.SubjectAlternativeName([
            # Describe what sites we want this certificate for.
            x509.DNSName(f"{user}.mysite.com"),
            x509.DNSName("www.mysite.com"),
            x509.DNSName("subdomain.mysite.com"),
        ]),
        critical=False,
        # Sign the CSR with our private key.
    ).sign(key, hashes.SHA256())
    with open(file_path, "wb") as f:
        f.write(csr.public_bytes(serialization.Encoding.PEM))
    send_request_AC2(user)
    certificate(user)


def certificate(user):
    # Cambiar al directorio AC2 antes de ejecutar openssl ca
    directorio_actual = os.getcwd()
    print(dir)
    os.chdir("../AC2")

    # Comando para ejecutar openssl ca
    password = "elbicho7"
    confirmacion = "y"
    confirmacion_2 = "y"
    comando_ca = f"openssl ca -in solicitudes/{user}_request.pem -notext -config AC2-72198.cnf"

    # Utilizar input para proporcionar las respuestas a las solicitudes interactivas
    entrada_interactiva = f"{password}\n{confirmacion}\n{confirmacion_2}\n"
    entrada_interactiva_bytes = entrada_interactiva.encode('utf-8')  # Codificar a bytes

    subprocess.run(comando_ca, input=entrada_interactiva_bytes, shell=True)

    # Restaurar el directorio de trabajo a su estado original

    lista_archivos = os.listdir("nuevoscerts")
    if lista_archivos:
        # Mover el primer (o único) archivo al directorio de certificados de usuario
        archivo_a_mover = lista_archivos[0]
        shutil.move(f"nuevoscerts/{archivo_a_mover}", f"../A/user_certificados/certificate_{user}.pem")
        print("Se movió el archivo correctamente.")
    else:
        print("No se encontraron archivos en nuevoscerts.")
    os.chdir(directorio_actual)


def send_request_AC2(user):
    print(user)
    comando = f"cp ../A/{user}_request.pem ../AC2/solicitudes"
    subprocess.run(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)


def verify_certificate(user):
    public_key = read_file(user, "public")
    certificado = ...
    try:
        public_key.verify(
            certificado.signature,
            certificado.tbs_certificate_bytes,
            # Depends on the algorithm used to create the certificate
            padding.PKCS1v15(),
            certificado.signature_hash_algorithm,
        )
    except InvalidSignature as e:
        raise e


def serialize(private_key):
    """Funcion que serializa una clave privada para poder guardarla en un fichero de salida asociado al usuario"""
    pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.BestAvailableEncryption(b'yeah_ivan')
    )
    return pem


def save_to_file(username, private_key):
    file_path = return_path("private", username)
    """Funcion encargada de guardar en un fichero asociado al usuario su clave privada serializada"""
    try:
        # Se serializa la clave privada
        priv_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.BestAvailableEncryption(b'yeah_ivan')
        )
        # Escritura en el archivo de la clave serializada
        with open(file_path, 'wb') as file:
            file.write(priv_pem)
        public_key = private_key.public_key()
        pub_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        file_path = return_path("public", username)
        # Escritura en el archivo de la clave serializada
        with open(file_path, 'wb') as file:
            file.write(pub_pem)
        print(f"Se ha guardado la clave para el usuario '{username}' en el archivo: {file_path}")
    # Captura de cualquier excepcion mediante depuracion por terminal
    except Exception as e:
        print(f"Error al guardar en el archivo: {e}")


def signing(mensaje, user):
    """Funcion que lleva a cabo el proceso de firma por el mensaje de la accion realizada por el usuario"""
    mensaje_bytes = mensaje.encode('utf-8')
    # Se lee la clave deserializada
    private_key = read_file(user, "private")
    # Proceso de firma
    signature = private_key.sign(
        mensaje_bytes,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    # Obtencion de la clave publica a partir de la clave privada
    return signature


def verify(user, signature, mensaje):
    # Obtencion de la clave publica
    public_key = read_file(user, "public")
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


def read_file(username, privacy_type):
    file_path = return_path(privacy_type, username)
    """Funcion encargada de leer un fichero que alberga una clave privada, y deserializarla"""
    try:
        if not os.path.exists(file_path):
            print(f"El archivo para el usuario '{username}' no existe.")
            return None
        with open(file_path, 'rb') as file:
            pem_content = file.read()
        # Si ha ido bien, se deserializa y devuelve el contenido de la clave privada
        print(f"Se ha leído el contenido del archivo para el usuario '{username}'.")
        content = deserialize(pem_content, privacy_type)
        return content
    # Trata de excepciones
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None


def return_path(privacy_type, username):
    if privacy_type == "public":
        directorio_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_absoluta = os.path.join(directorio_actual, '..', 'user_public_files')
        file_path = os.path.join(ruta_absoluta, f"{username}_public_key.pem")
    elif privacy_type == "private":
        directorio_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_absoluta = os.path.join(directorio_actual, '..', 'user_private_files')
        file_path = os.path.join(ruta_absoluta, f"{username}_private_key.pem")
    else:
        return " "
    return file_path


def return_deserialized_cert(username):
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_absoluta = os.path.join(directorio_actual, '..', 'A', 'user_certificados')
    file_path = os.path.join(ruta_absoluta, f"certificate_{username}.pem")
    with open(file_path, 'rb') as file:
        pem_content = file.read()
    cert = x509.load_pem_x509_certificate(pem_content)
    return cert


def deserialize(data, privacy_type):
    if privacy_type == "public":
        key = load_pem_public_key(data)
        return key
    """Funcion que lleva a cabo la tarea de deserializar una clave 'data' junto a su password asociado"""
    private_key = serialization.load_pem_private_key(
        data,
        password=b'yeah_ivan',
        backend=default_backend()
    )
    return private_key


if __name__ == "__main__":
    user = "ili33"
    generate_key(user)
    key = read_file(user, "private")
    certificate_request(user, key)
