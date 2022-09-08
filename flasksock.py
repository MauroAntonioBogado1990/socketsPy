from flask import Flask
from flask_sockets import Sockets

#Agregamos la app y el socket
app = Flask(__name__)
sockets = Sockets(app)

#Agregamos nuestro decorador 
@sockets.route('/')
def echo(ws):#usamos la definicion de echo,le pasamos como parametro webscoket 
    while not ws.closed:
        message = ws.receive() #recibimos el mensaje
        print('message received:', message)
        ws.send(message + '/server')

from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler
server = pywsgi.WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
server.serve_forever()
