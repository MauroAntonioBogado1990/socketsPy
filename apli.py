from fastapi import FastAPI, WebSocket

#creacion de la app
app = FastAPI()

#endpoint que vamos a recibir
@app.websocket('/')
async def echo(websocket: WebSocket):
    #se acepta el socket
    await websocket.accept()
    
    #loop de espera, envio de respuesta
    while True:
        data = await websocket.receive_text()
        print('message received:', data)
        await websocket.send_text(data + '/server')
