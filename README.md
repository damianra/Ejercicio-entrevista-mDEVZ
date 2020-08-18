# Ejercicio-entrevista-mDEVZ
<br>
Para que el proyecto funcione, es necesario tener instalado python3.7+
<p>Descripción:</p>
<p>Sitio en Django 2.2, Ejercicio para entrevista de trabajo empresa mDEVZ, utilizando javascript para obtener datos de busquedas de Twitter y las imprime en un div en pantalla, contiene una base de datos en MySQL llamada Ejercicio_mDEVZ con una tabla donde guarda las busquedas realizadas.</p>
<p>URLs:<br>
http://127.0.0.1:8000<br>
http://127.0.0.1:8000/hist/
</p>
<br>
<h3>Procedimientos de despliegue de proyecto:</h3>
<br>
1) Instalar python 3.7 (https://www.python.org/downloads/)<br>
---- recomendable instalar requerimientos desde virtualenv ---<br>
(Instalar virtualenv: pip3 install virtualenv)<br>
(Crear entorno virtual: Desde el directorio dónde se encierra el archivo mánager.py ejecutar<br>
virtualenv venv -p python3)<br>
(Iniciar el entorno virtual source venv/bin/activate)<br>
(Para desactivar entorno virtual source venv/bin/deactivate)<br>
--------- Esto es necesario si no queremos instalar todo en nuestro S.O.------<br>

2) Instalar los requerimientos del proyecto usando "pip": pip install -r requirements.txt<br>
3) Importar archivo .sql a la base de datos (los datos de conexion se encuentran en el archivo settings.py en la carpeta Ejercicio_mDEVZ la base de datos contiene el nombre de Ejercicio_mDEVZ)<br>
4) Añadir las credenciales de Twitter API en el archivo Ejercicio-entrevista-mDEVZ/tweetapp/views/views.py en la clase SearchAPIView
5) Por cmd (windows) o terminal (linux) ejecutar el proyecto en la carpeta raiz del proyecto (donde se encuentra el archivo manage.py): python manage.py runserver<br>
6) El servidor por defecto se ejecuta en la url 127.0.0.1:8000/<br>
<br>
<br>
<p>El proyecto contiene dos urls mas de las pedidas una para obtener los datos filtrados y otra para ver el historial y añadir las busquedas realizadas:</p>
<p>http://127.0.0.1:8000/v1/search/?query={"PARAMETRO DE BUSQUEDA"} donde se le envia el parametro de busqueda y devuelve en JSON los datos necesarios (no todos) para completar la vista, obtiene hasta 10 busquedas</p>
<p>La segunda url agregada http://127.0.0.1:8000/v1/history/ el cual por metodo GET devuelve las busquedas realizadas y por POST añade nuevas busquedas</p>
