### Copias de seguridad
## Ejercicio 1.
# Paso 1
Me dirijo a la carpeta en la que tengo el docker-compose.yml con el comando
PS C:\Users\PC> cd C:\Odoo
# Paso 2
docker-compose exec db bash
# Paso 3
Ejecuto el comando: service postgresql stop
# Paso 4
Salgo del contenedor con el comando exit
# Paso 5
Creo la copia de seguridad: pg_dump -U odoo postgres > backup.sql
# Paso 6
Compruebo que existe la copia de seguridad con ls - l
# Paso 7
Uso el comando docker cp db:/backup.sql C:/Odoo/dataPg/backup.sql
para copiar el archivo backup.sql del contenedor al anfitrion.
# Paso 8
Uso el comando exit
# Paso 9
Uso el comando psql -U odoo odoo < backup.sql y arroja el resultado:

SET
SET
SET
SET
SET
 set_config
------------

(1 row)

SET
SET
SET
SET
postgres@41920dc6cca2:/$