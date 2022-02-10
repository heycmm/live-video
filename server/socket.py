from flask_socketio import SocketIO, emit
import json
import time
from camera.camera import Camera
socketio = SocketIO(async_mode='eventlet',cors_allowed_origins='*')
camera = Camera()
"""
socket 协议播放服务
"""

@socketio.on('video')
def send_video(data):

    time.sleep(0.01)
    data = json.dumps({
        'img_url': camera.read()
    })
    emit('video', data, json=True)