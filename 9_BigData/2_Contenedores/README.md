Ejemplo realizado para el trabajo con Dockers VS metodo normal 
(entorno virtual + ejecucion) para una aplicacion con **fastAPI**

- Metodo normal:
    -
    - Creación de entorno virtual:
        - pip install uvicorn[standard]
        - pip install fastapi
    - Ejecutar plicación:
        - uvicorn main:app --reload

- Metodo Dockers:
    -
    - Crear archivo: 'Dockerfile'
    - Añadir importaciones necesarias para la ejecución de la 
    aplicación en 'Dockerfile'
    - Crear imagen Docker (instruccion + nombre):
        - docker build -t master_eip/ej_fastAPI ./
    - Ejecutar docker:
        - docker run -d --name app -p 80:80 nombre repositorio
        - En segundo plano: -d
        - Nombre app dentro docker: --name
        - Puerto interno y externo_ -p
 
    ***Nota:*** *Docker file esta en el mismo directorio que App*

- Docker Compose
    -
    - Crear archivo "docker-compose.yml" en directorio proyecto
    - Crear imagen: (estando en el directorio del proyecto)
        - docker-compose build
    - Ejecutar imagen: (estando dentro del directorio del proyecto)
        - docker-compose up
        
- EXTRA DOCKER
    - 
    - Comprobar imagenes creadas:
        - docker images
    - Comprobar si se ha lanzado servicio:
        - docker ps
    - Detener proceso:
        - docker kill container
        - docker stop container       
    - Eliminar container si ya existe:
        - docker rm container name
    - Conocer la info de nuestro docker:
        - docker system df
    - Limpiar docker:
        - Eliminar toda informacion del sistema que se este ejecutando de forma activa: docker system prune
        - Eliminar los volumenes: docker volume prune
        - Eliminar el cache creado: docker builder prune
    - Eliminar imagen:
        - docker image rm -f name
        - forzar borrado: -f
        
