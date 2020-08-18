# Ejercicio-entrevista-mDEVZ
<br>
Para que el proyecto funcione, es necesario tener instalado python3.7+
<br>
<h3>Procedimientos de despliegue de proyecto:</h3>
<br>
1) Instalar python 3.7 (https://www.python.org/downloads/)<br>
2) Instalar los requerimientos del proyecto usando "pip": pip install -r requirements.txt<br>
3) Importar archivo .sql a la base de datos (los datos de conexion se encuentran en el archivo settings.py en la carpeta Ejercicio_mDEVZ la base de datos contiene el nombre de Ejercicio_mDEVZ)<br>
4) Por cmd (windows) o terminal (linux) ejecutar el proyecto en la carpeta raiz del proyecto (donde se encuentra el archivo manage.py): python manage.py runserver<br>
5) El servidor por defecto se ejecuta en la url 127.0.0.1:8000/<br>
<br>
<br>
<p>El proyecto contiene dos urls mas de las pedidas una para obtener los datos filtrados y otra para ver el historial y añadir las busquedas realizadas:</p>
<p>http://127.0.0.1:8000/v1/search/?query={"PARAMETRO DE BUSQUEDA"} donde se le envia el parametro de busqueda y devuelve en JSON los datos necesarios (no todos) para completar la vista, obtiene hasta 10 busquedas</p>
<p>La segunda url agregada http://127.0.0.1:8000/v1/history/ el cual por metodo GET devuelve las busquedas realizadas y por POST añade nuevas busquedas</p>
