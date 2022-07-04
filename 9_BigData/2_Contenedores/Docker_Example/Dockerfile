# Version de Python a emplear
FROM python:3.8

# Librerias que se necesita e instruccion de instalacion
RUN pip install fastapi uvicorn[standard]

# Puerto que queremos exponer
EXPOSE 80

# Copiar estructura de app en directorio en estructura app de Docker
COPY ./App /app

# Comandos a emplear:
# - Acceder a database_creator.py de app en Docker
# - Activar el host interno y externo: 0.0.0.0
# - Puerto de comunicación: 80
CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","80"]