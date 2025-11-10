
## Instalación

Instalar pip y python duh 

Descargar proyecto 

Entrar a cmd donde guardaste el proyecto

Instalar dependencias `pip install -r requirements.txt`

Correr aplicación en consola con `py Parcial02_MariaAcevedo.py` 

Entrar a http://127.0.0.1:5000/calcular/numeroDeseado <- insertar el numero que deeses

## Cómo modificaría el diseño si el microservicio tuviese que comunicarse con otro servicio que almacena el historial de calculos en una base de datos externa: 

Modificaría el diseño para incluir una llamada HTTP al segundo servicio. Después de calcular el factorial y determinar si es par o impar el número, el microservicio enviaría los datos como JSON mediante una solicitud POST.

El otro servicio tendría que importar un request para recibir los datos y guardarlos. Ambos servicios se pueden coordinar fácilmente con Docker Compose.

Esto permite separar responsabilidades: uno calcula, el otro almacena. Y si hace falta, usaría Docker para empaquetar todo.

:D
