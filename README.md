
## Instalación

Instalar pip y python duh 

Descargar proyecto 

Entrar a cmd donde guardaste el proyecto

Instalar dependencias `pip install -r requirements.txt`

Correr aplicación en consola con `py Parcial02_MariaAcevedo.py` 

Entrar a http://127.0.0.1:5000/calcular/numeroDeseado <- insertar el numero que deeses

## Cómo modificaría el diseño si el microservicio tuviese que comunicarse con otro servicio que almacena el historial de calculos en una base de datos externa: 

Modificaría el diseño para incluir una comunicación HTTP entre microservicios.
Después de calcular el factorial y determinar si el número es par o impar, el microservicio actual enviaría los datos en formato JSON mediante una solicitud POST al segundo servicio.

El segundo servicio recibiría estos datos (por ejemplo, usando requests o un endpoint Flask con método POST) y los almacenaría en una base de datos externa.

Ambos microservicios podrían coordinarse mediante Docker Compose, lo que permitiría definir fácilmente la red interna y los contenedores de cada uno.

Este enfoque separa responsabilidades: un servicio se encarga del cálculo, mientras que el otro maneja el almacenamiento y el historial.
Si fuera necesario, empaquetaría ambos servicios con Docker para facilitar su despliegue y portabilidad.
