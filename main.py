
from flask import Flask
from server import socketio

def create_app():
    app = Flask(__name__)
    socketio.init_app(app)
    return socketio, app


if __name__ == "__main__":

    socketio, app = create_app()
    socketio.run(app=app, host='127.0.0.1', port='4242')