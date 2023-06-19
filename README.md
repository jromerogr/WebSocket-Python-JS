# Descripción
Aplicación que contiene un servidor de websocket desarrollado en **Python** y un cliente de websocket desarrollado en **JavaScript** y **HTML**
# Pre-requisitos
Para que el servidor de websocket funcione correctamente hay que instalar las dependencias necesarias con el siguiente comando: `pip install -r requirements.txt`
# Ejecución
- Para lanzar el servidor de websocket únicamente hay que ejecutar el script de Python que se encuentra en la ruta relativa: `server/websocketServer.py`
- Para lanzar el cliente de websocket únicamente hay que abrir en un navegador el archivo HTML que se encuentra en la ruta `client/index.html`
# Funciones
- Desde el cliente de websocket se realiza la conexión automáticamente con el servidor de websocket
- Desde el cliente de websocket se pueden mandar mensajes al servidor de websocket con el formualario disponible
- Los mensajes que devuelve el servidor al cliente se muestran en la consola del navegador
- Se pueden mandar mensajes a todos los clientes conectados enviando un mensaje que comience por `!all` . Por ejemplo. `!all Hola a todos`