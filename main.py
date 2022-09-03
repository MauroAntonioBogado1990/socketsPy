from aiohttp import web,WSMsgType

#realizamos la llamada 
async def echo(request):
    ws = web.WebSocketResponse()
    #espramos la respuesta
    await ws.prepare(request)
    #realizamos el for para recorrer la petición,
    # donde para la petición y espera 
    async for msg in ws:
          #realizo la lectura del message  
          if msg.type == WSMsgType.TEXT:
            if msg.data == 'close':
                await ws.close()
            else:
                print('message received', msg.data)
                await ws.send_str(msg.data + '/server')    
    return ws

#configuramos y corremos la app
app = web.Application()
app.router.add_get('/', echo)
web.run_app(app)

