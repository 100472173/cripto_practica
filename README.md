# cosas_que_hacer_en_la_app

1. Frame de mostrar datos
2. Comprobar la sintaxis de registro
3. Casos de errores



# cosas_que_hacer_cifrado
Cuando insertemos el usuario en la bbdd, tiene que haber un campo de KEY (clave unica)
    -Generamos la clave, ciframos todos los datos con esa clave, y almacenamos la clave, encriptandola con una maestra.

No ciframos usuario. De esa forma, podemos buscarlo en la BBDD.
    -Buscamos el usuario, verificamos la contra, y si esta en la BBDD -> se hace login, se seleccionan sus datos, claves, etc
     y se muestran por pantalla.
