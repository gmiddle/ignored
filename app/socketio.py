from flask_socketio import SocketIO, emit, join_room
import os


# configure cors_allowed_origins
if os.environ.get('FLASK_ENV') == 'production':
    origins = [
        'http://ignored-group4.herokuapp.com',
        'https://ignored-group4.herokuapp.com'
    ]
else:
    origins = "*"

# initialize your socket instance
socketio = SocketIO(cors_allowed_origins=origins)


# handle chat messages
@socketio.on("chat")
def handle_chat(data):
    emit("chat", data, broadcast=True)

@socketio.on("delete")
def handle_chat(data):
    emit("delete", data, broadcast=False)

# # handle joining chat rooms
# @socketio.on("join")
# def join_chat(data):
#     username = data["user"] 
#     server_room = data["room"] # passing in info on room
#     join_room(server_room)
#     emit("broadcast_message", data, room=server_room, broadcast=True)
