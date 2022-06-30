# Proyecto-2-Operativos
Tarea Programada #2 EIF212 – Sistemas Operativos
### Integrantes: 
-> Norman Betancourtt  <br />
-> Rebeca Servellon <br />
-> Hector Mendez <br />

## Instalación
Se deben de correr los comandos  `pip install -r requirements.txt` y  ' pip install googletrans==4.0.0rc1 ' y 
se instalaran las dependencias necesarias para el correcto funcionamiento de este

##Descripcion
El programa se basa en una arquitectura cliente servidor que permitira mutiples conexiones de clientes simultaneamente
El servidor proveera un servicio el cual sera en este caso la traduccion de frases en español a casi cualquier idioma dependiendo del 
codigo que se ingrese
en = english
fr= french
it = italian
ja = japanese
pt = Portuguese
es = Spanish
etc...
## Uso
1) Correr el archivo `server/server.py` (servidor)
2) Correr el archivo `client/main.py`    (cliente)
3) El cliente le solicitará una palabra para traducir, usted la introduce ** 
4) El formato del mensaje que se le debe de enviar al servidor desde el cliente para realizar la traduccion es 'codIdioma-frase'
ejm: 
'fr-Hola Mundo!'  (Se recibira como respuesta 'salut monde!')
'en-Hola Mundo!'  (Se recibira como respuesta 'Hello world!')
