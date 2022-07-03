# Proyecto-2-Operativos
Tarea Programada #2 EIF212 – Sistemas Operativos
### Integrantes: 
-> Norman Betancourtt  <br />
-> Rebeca Servellon <br />
-> Hector Mendez <br />

## Instalación
Lo primero que se tiene que realizar es descargar la imagen de docker que se encuentra en el siguiente 
link: <a> https://hub.docker.com/repository/docker/htrmf/firstimage </a>
Esta imagen proveera la aplicacion que correra del lado del servidor

Lo segundo descargar este repositorio de git, mas especificamente la carpeta de client que posee el archivo main.py que correra del lado del cliente

##Descripcion
El programa se basa en una arquitectura cliente servidor que permitira mutiples conexiones de clientes simultaneamente.
El servidor proveera un servicio el cual sera en este caso la traduccion de palabras y frases en español a casi cualquier idioma dependiendo del 
codigo que se ingrese <br />
en = english <br />
fr= french <br />
it = italian <br />
ja = japanese <br />
pt = Portuguese <br />
es = Spanish <br />
etc...

## Uso
1) Correr la imagen que se descargo para activar el servidor que ofrecera el servicio de traducciones (servidor)
2) Correr el archivo `client/main.py`    (cliente)
3) Una vez teniendo el archivo main.py corriendo, usted como cliente debe de insertar una frase o palabra para que realice la traduccion al idioma
que se selecciono
4) El formato del mensaje que se le debe de enviar al servidor desde el cliente para realizar la traduccion es 'codIdioma-frase'
ejm:  <br />
'fr-Hola Mundo!'  (Se recibira como respuesta 'Salut Monde!') <br />
'en-Hola Mundo!'  (Se recibira como respuesta 'Hello world!') <br />
'ja-Hola Mundo!'  (Se recibira como respuesta '「こんにちは世界」')
