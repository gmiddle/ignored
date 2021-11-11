
from flask import Blueprint, jsonify, Flask, redirect, request
from flask_login import login_required, current_user
from app.forms import ServerForm
from app.models import Server, PrivateServer, db, User
from werkzeug.security import generate_password_hash

server_routes = Blueprint('servers', __name__)
private_server_routes = Blueprint('private_servers', __name__)
# GET all routes
@server_routes.route('/')
def servers():
    servers = Server.query.all()
    print("hit", current_user)
    return {'servers': [server.to_dict() for server in servers]}


@private_server_routes.route('/')
def private_servers():

    private_servers = PrivateServer.query.all()
    return {'servers': [private_server.to_dict() for private_server in private_servers]}

# GET by Id routes
@server_routes.route('/<int:id>')
def server(id):
    server = Server.query.get(id)
    return server.to_dict()


@private_server_routes.route('/<int:id>')
def private_server(id):
    private_server = PrivateServer.query.get(id)
    return private_server.to_dict()

# POST a server
@server_routes.route('/', methods=['POST'])
def servers_post():
  """
  Creates a new server
  """

  form = ServerForm()

  form['csrf_token'].data = request.cookies['csrf_token']


  if form.validate_on_submit():
    server = Server(
      name=form.data['name'],
      description=form.data['description'],
      serverImg=form.data['serverImg'],
      serverInviteKey = generate_password_hash(f"{form.data['name']}")[-7:-1].upper(),
      ownerId = current_user.id
    )
    user = User.query.get(server.ownerId)
    db.session.add(server)
    user.serverList.append(server)
    db.session.commit()
    print(server.to_dict(), '-------------------------------')
    return server.to_dict()
  else:
    print(form.errors)
    return "Bad data"


# POST a private_server
# @private_server_routes.route('/', methods=['POST'])
# def private_server_post():
#   pass

# PUT edit server
@server_routes.route('/edit/<int:id>', methods=['PUT'])
def servers_edit(id):
  server_edit = Server.query.get_or_404(id)
  form = ServerForm()
  if form.validate_on_submit():
    server_edit.name = form.data['Name'],
    server_edit.description = form.data['Description'],
    server_edit.serverImg = form.data['ServerImg']
  try:
    db.session.commit()
    return redirect('/')
  except:
    print(form.errors)
    return "Bad data"


@server_routes.route('/delete/<int:id>', methods=['DELETE'])
def server_delete(id):
  server = Server.query.filter(Server.id == id).first()
  try:
    db.session.delete(server)
    db.session.commit()
    return "Server Deleted"
  except:
<<<<<<< HEAD
    return "No Server Found"
=======
    return "Server not Found"
>>>>>>> main
