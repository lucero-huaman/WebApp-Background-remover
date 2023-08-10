WebApp removedora de fondos
===========================

Instalar
--------

### Crear entorno virtual

 Es una buena práctica trabajar con entornos virtuales para mantener tus dependencias de proyecto separadas y organizadas.   
Para configurar un entorno virtual se deben seguir los siguientes pasos:  
 Abrir una terminal dentro de Visual Studio. Se puede realizar ello seleccionando "Terminal" en el menú "Ver".  
 Ejecuta el siguiente comando para crear un nuevo entorno virtual: python -m venv venv Se activa el entorno virtual con los siguientes comandos:  

 ```
 venv\\Scripts\\activate
 ```

Instalar Flask 
---------------

 Una vez activado el entorno virtual para crear la aplicación web se usará Flask empleando lso siguientes comandos en la terminal. 
 
 ```
 pip install flask
 ```

### Instalar librerías

 Para el procesamiento de imágenes se usará rembg, la cual es una biblioteca de python que utiliza técnicas de aprendizaje automático y redes neuronales para realizar la segmentación semántica de imágenes y detectar el objeto que se debe conservar.   
 Para poder instalarla se usarán los siguiente comandos. 
 
 ```
 pip install rembg
 ```

Web
---

### Interfaz principal

 Se diseñó la interfaz en figma, para el frotn se uso HTML y CSS, mientras que para la parte lógica se uso python con ayuda de Flask.

 ![interfaz principal](https://iili.io/HDJHye1.jpg)
 
 ### Carga de imágenes

 Las imágenes pueden ser subidas arrastrando estas a la zona señalada o dando click a Seleccionar archivo, una vez realizado ello se da click a Remover fondo.

 ![carga de imagen 1](https://iili.io/HDJqPiF.jpg) ![carga de imagen 2](https://iili.io/HDJqbNp.jpg)
 
 ### Resultados

Se puede observar el antes y después de las pruebas realizadas.

Prueba 1
  
 ![a d prueba 2](https://iili.io/HDJB55x.png)

Prueba 2

 ![a d prueba 1](https://iili.io/HDJBBb2.png)