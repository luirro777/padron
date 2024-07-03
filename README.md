
# PADRON

## Aplicación para consulta de lugar de votación

Esta aplicación permite consultar el lugar de votación de una persona utilizando su DNI.

## Instalación

### Requisitos previos

Asegúrate de tener instalada la herramienta para creación de entornos virtuales:

```bash
sudo apt install python3-virtualenv
```

### Descargar y configurar la aplicación

Clona el repositorio:

```bash
git clone https://github.com/luirro777/padron
cd padron
```

Crea y activa un entorno virtual:

```bash
virtualenv ./padron-venv
source ./padron-venv/bin/activate
```

Instala las dependencias y configura la base de datos:

```bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
```

### Ejecutar el servidor de desarrollo

Lanza el servidor local:

```bash
python manage.py runserver
```

La aplicación estará disponible en [http://127.0.0.1:8000/](http://127.0.0.1:8000/). Puedes detener el servidor con Ctrl + C.

## Administración de la base de datos

### Crear un superusuario

Primero, crea un superusuario para acceder al panel de administración:

```bash
python manage.py createsuperuser
```

Inicia el servidor y accede a [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) para iniciar sesión con las credenciales del superusuario.

### Crear y gestionar Mesas

En el panel de administración, crea Mesas especificando los siguientes campos:

* numero
* denominacion
* direccion
* provincia
* departamento
* localidad
* ubicacion_geografica (URL de Google Maps)

Para obtener la URL de ubicación geográfica, busca la dirección en [Google Maps](https://maps.google.com), haz clic en "Compartir" y copia la URL proporcionada.

### Añadir Afiliados

Después de crear Mesas, puedes añadir Afiliados especificando:

* apellidos
* nombres
* dni
* organizacion
* mesa (número de mesa)

### Poblar la base de datos vía comandos

También puedes importar datos utilizando archivos CSV. Prepara archivos CSV con el siguiente formato:

#### Mesas.csv

```plaintext
numero,provincia,departamento,descripcion,direccion,localidad,ubicacion_geografica
1,Cordoba,Capital,La mesa de todos,Calle falsa 123,Cordoba,https://maps.app.goo.gl/direccionficticia
```

#### Afiliados.csv

```plaintext
dni,apellidos,nombres,organizacion,mesa
12345678,perez,juan,Orga de Juan,3
```

Importa los datos utilizando los siguientes comandos:

```bash
python manage.py import_mesas Mesas.csv
python manage.py import_afiliados Afiliados.csv
```

## Funcionalidades adicionales

Accede a otras funcionalidades mediante el login en [http://127.0.0.1:8000/login](http://127.0.0.1:8000/login):

* Lista de mesas
* Padron completo
* Consulta (redirección a la página principal de la aplicación)
* Salir (logout)

En "Lista de mesas", puedes acceder a opciones adicionales como la generación del padrón en formato PDF.

## TODO

Agregar instrucciones para despliegue en producción.

## Contacto

Para preguntas o sugerencias, contáctame en luisromano@gmail.com.



