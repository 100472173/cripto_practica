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

# Ejemplo de depuracion
write_file("Jose", bytes("12345", encoding="UTF-8"))
