import asyncio
import websockets

# URL y puerto donde se aloja el servidor de websocket
URL = "localhost"
PORT = 8765
# Listdo con todos los clientes conectados
active_connetions = []

# Función que gestiona las conexiones y mensajes de los clientes
async def handle_connection(websocket):
    # Se añade el nuevo cliente al listado de conexiones activas
    active_connetions.append(websocket)
    print("Nuevo cliente. Total: "+str(len(active_connetions)))

    
    try:
        # Se trata el mensaje enviado por el cliente
        async for message in websocket:
            print("El cliente ha mandado el mensaje: "+message)
            if(message.startswith("!all")):
                await send_to_all(message[4:])
            await websocket.send("Mensaje Recibido")
    finally:
        # Cuando el cliente cierra la conexión se elimina del listado de conexiones activas
        print("Un cliente ha cerrado la conexion")
        active_connetions.remove(websocket)

# Función que envía un mensaje a todos los clientes conectados
async def send_to_all(message):
    for connection in active_connetions:
        await connection.send(message)

# Se inicia el servidor indicando la función que gestiona las conexiones y la URL y puerto donde se lanza el servidor
start_server = websockets.serve(handle_connection,URL,PORT)

# Se inicia el bucle "indefinido"
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()