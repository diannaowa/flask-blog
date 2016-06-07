from flask import Flask
from flask_sockets import Sockets


from dockerc import ws as ws_blueprint
app = Flask(__name__)
sockets = Sockets(app)
sockets.register_blueprint(ws_blueprint,url_prefix='/ws')



if __name__ == "__main__":
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    server = pywsgi.WSGIServer(('', 8000), app, handler_class=WebSocketHandler)
    server.serve_forever()