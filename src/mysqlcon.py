import mysql.connector

# Configura la conexión
config = {
    'user': 'tu_usuario',
    'password': 'tu_contraseña',
    'host': 'localhost',
    'database': 'tu_base_de_datos',
    'raise_on_warnings': True
}

# Intenta establecer la conexión
try:
    connection = mysql.connector.connect(**config)
    if connection.is_connected():
        print('Conexión establecida correctamente')
except mysql.connector.Error as err:
    print(f'Error: {err}')
finally:
    # Cierra la conexión al finalizar
    if 'connection' in locals():
        connection.close()
        print('Conexión cerrada')

'''Procedimiento para conexion:

Inicia XAMPP:
Abre el panel de control de XAMPP y asegúrate de que el módulo MySQL esté activado.

Abre phpMyAdmin:
En el panel de control de XAMPP, haz clic en el botón "Admin" junto al módulo MySQL. Esto abrirá phpMyAdmin en tu navegador web.

Accede a la sección de usuarios:
En phpMyAdmin, busca una pestaña o sección llamada "Usuarios" o "Users" en inglés. Aquí es donde encontrarás la información sobre los usuarios de la base de datos.

Revisa los detalles del usuario:
Busca el usuario que estás utilizando para conectarte a la base de datos desde Python. Allí encontrarás información como el nombre de usuario (User), el servidor al que tiene acceso (Host), y la base de datos a la que tiene acceso (Database).


En este ejemplo, encontrarás la información de conexión bajo la columna "Edit Privileges" para cada usuario.

Anota la información de conexión:
Asegúrate de anotar el nombre de usuario (User), la contraseña (Password), el servidor (Host), y la base de datos (Database). Estos son los datos que necesitarás en tu código Python para establecer la conexión.

Con esta información, puedes completar la sección de configuración en tu código Python, como se mencionó en el paso 7 del mensaje anterior. Recuerda reemplazar 'tu_usuario',
 'tu_contraseña', y 'tu_base_de_datos' con los valores específicos que encuentres en phpMyAdmin.
 
 Obtener IP Pública
 
 
Si deseas conectarte a una base de datos MySQL en XAMPP desde otro ordenador a través de Internet en lugar de utilizar localhost, hay algunos pasos adicionales que debes seguir. Aquí tienes una guía básica:

Configurar MySQL para aceptar conexiones remotas:

Abre el archivo de configuración de MySQL, que generalmente se encuentra en la carpeta xampp\mysql\bin y se llama my.ini o my.cnf.

Busca la sección [mysqld] y asegúrate de que la línea bind-address esté comentada o establecida en 0.0.0.0:


#bind-address = 127.0.0.1 👉 REVISADO, ESTÁ COMENTADO
Reinicia el servidor MySQL desde el panel de control de XAMPP después de realizar cambios en la configuración.

Asegurar el acceso remoto al usuario de la base de datos:

Accede a phpMyAdmin desde tu navegador en http://localhost/phpmyadmin/.
Selecciona la base de datos a la que deseas acceder de forma remota.
Ve a la pestaña "Usuarios" y edita el usuario que estás utilizando para la conexión remota.
Asegúrate de que este usuario tenga permisos para conectarse desde la dirección IP del otro ordenador.
Obtener tu dirección IP pública:

En el ordenador donde está ejecutándose XAMPP, puedes buscar tu dirección IP pública en un motor de búsqueda, por ejemplo, "What is my IP". Anota la dirección IP pública.
Modificar el código Python para usar la dirección IP:

En tu código Python, donde defines la configuración de la conexión, reemplaza 'localhost' con la dirección IP pública que obtuviste:
python
Copy code
config = {
    'user': 'tu_usuario',
    'password': 'tu_contraseña',
    'host': 'tu_direccion_ip_publica',
    'database': 'tu_base_de_datos',
    'raise_on_warnings': True
}
Configurar el firewall:

Asegúrate de que el firewall en el equipo que ejecuta XAMPP permita el tráfico en el puerto MySQL (por defecto, el puerto 3306).
Reiniciar XAMPP:

Reinicia XAMPP para aplicar los cambios.
 '''