from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import Message, PrivateMessage

message_routes = Blueprint('messages', __name__)
private_message_routes = Blueprint('private_messages', __name__)
# GET all routes
@message_routes.route('/')
def messages():
    messages = Message.query.all()
    return {'messages': [message.to_dict() for message in messages]}


@private_message_routes.route('/')
def private_messages():
    private_messages = PrivateMessage.query.all()
    return {'messages': [private_message.to_dict() for private_message in private_messages]}

# GET by Id routes
@message_routes.route('/<int:id>')
def server(id):
    message = Message.query.get(id)
    return message.to_dict()


@private_message_routes.route('/<int:id>')
def private_message(id):
    private_message = PrivateMessage.query.get(id)
    return private_message.to_dict()


