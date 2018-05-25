# bk-backend

Administrador Web para APP de Burger King Ecuador

# Tecnologías
- Django 1.11 para Python 3
- PostgreSQL DataBase

# Instalación 
Una vez clonado el proyecto de https://github.com/jrealpe/bk-backend.git
1. Crear un entorno virtual para python3.
   En windows o Linux ejecute el comendo: 
   ``` 
   cd bk-backend
   python -m venv [nombre_de_virtualvenv]
   ```
   Si tiene python3 en su máquina no tendrá problemas con lo anterior. 
   Pero si tiene instalado también python2 debe especificar la ruta al archivo elecutable de python3 para la correcta definición del entorno virtual, así: C:\Python36\python en lugar de sólo python.

2. Ejecute el entorno virtual.
    En el directorio donde creó el virtualenv:
    - En Windows utilice el comando: ```[nombre_de_virtualenv]\Scripts\activate```
    - En Linux:  ```source [nombre_de_virtualenv]/bin/activate```

3. Instale todas las dependencias del proyecto
   ```
   pip install -r requirements.txt
   ```

 4. Actualice la base de datos local
    ```
    python manage.py migrate
    ```
 Opcional: En lugar del paso 4 y 5 puede ejecutar el Makefile con el comando ``` make ``` 
 
 5. Ejecutar el proyecto
    ```
    python manage.py runserver
    ```

