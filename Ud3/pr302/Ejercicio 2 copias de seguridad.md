### Ejercicio 2 copias de seguridad
## Paso 1
Me dirijo a la carpeta en la que tengo el docker-compose.yml
## Paso 2
Abro una terminal y ejecuto el comando docker compose up
## Paso 3 
Voy al enlace http://localhost:8069/web/database/manager
## Paso 4
Pulso sobre el icono Backup, introduzco la Master Password,pulso el botón Backup
y se descarga un archivo.
## Paso 5
Elimino los contenedores y todo lo que hay en las carpetas dataPG, sessions,y addons
## Paso 6
Voy de nuevo a http://localhost:8069/web/database/manager
## Paso 7
Pulso en Restore Database
## Paso 8
Introduzco la Master Password y selecciono el archivo que se descargo anteriormente
