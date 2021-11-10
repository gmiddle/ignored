from flask import Blueprint, jsonify, redirect, request
from flask_login import login_required, current_user
from app.forms import MessageForm
from app.models import Message, PrivateMessage, channel, db, Channel

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


# POST a message
@message_routes.route('/', methods=['POST'])
def message_post():
  """
  Creates a new message
  """
  form = MessageForm()

  if form.validate_on_submit():
    new_message = Message(
      content = form.data["Content"],
      user_id = current_user.id,
      profilePic = current_user.profilePic
    )
    db.session.add(new_message)
    db.session.commit()
    return redirect('/')
  else:
    print(form.errors)
    return "Bad data"


# POST a private message
@private_message_routes.route('/', methods=['POST'])
def private_message_post():
  """
  Creates a new private message
  """
  form = MessageForm()

  if form.validate_on_submit():
    private_message = PrivateMessage(content=form.data["Content"])
    db.session.add(private_message)
    db.session.commit()
    return redirect('/')
  else:
    print(form.errors)
    return "Bad data"

# PUT edit message
@message_routes.route('/edit/<int:id>', methods=['PUT'])
def message_edit(id):
  message = Message.query.get_or_404(id)
  form = MessageForm()
  if form.validate_on_submit():
    message.content = form.data["Content"]
  try:
    db.session.commit()
    return redirect('/')
  except:
    print(form.errors)
    return "Bad data"

# PUT edit private message
@private_message_routes.route('/edit/<int:id>', methods=['PUT'])
def private_message_edit(id):
  private_message = PrivateMessage.query.get_or_404(id)
  form = MessageForm()
  if form.validate_on_submit():
    private_message.content = form.data["Content"]
  try:
    db.session.commit()
    return redirect('/')
  except:
    print(form.errors)
    return "Bad data"

# DELETE a message by id
@message_routes.route('/delete/<int:id>', methods=['DELETE'])
def delete_message():
  message = Message.query.get_or_404(id)
  try:
    db.session.delete(message)
    db.session.commit()
    return redirect('/')
  except:
    return "Message not found."

# DELETE a private message
@private_message_routes.route('/delete/<int:id>', methods=['DELETE'])
def delete_private_message():
  private_message = PrivateMessage.query.get_or_404(id)
  try:
    db.session.delete(private_message)
    db.session.commit()
    return redirect('/')
  except:
    return "Message not found."

