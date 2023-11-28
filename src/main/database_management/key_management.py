"""Por una anomalia dado el alacance de la practica, la clave maestra se almacena en la siguiente clase encapsulada
   como un atributo privado de acceso al no figurar esta como parametro o variable de entorno
 """


class MasterKey:
    def __init__(self):
        """Cada vez que se instancia la clase, se crea un objeto con un atributo privado que almacena
         la clave maestra"""
        self.__data = b'=6\x90\x9e\x02#d\x8f\x02\xcd\x19|\xdd\x05Dj\x18\x8cG\xf5\x1fZ\x02\xc6\x0cLS\xd8\xa6;c\x8e'

    @property
    def data(self):
        """Tenemos un getter para poder acceder a los datos"""
        return self.__data
