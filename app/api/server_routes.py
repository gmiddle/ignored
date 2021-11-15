from flask import Blueprint, request
from flask_login import login_required, current_user
from app.forms import ServerForm
from app.models import Server, PrivateServer, db, User, Channel
from werkzeug.security import generate_password_hash

server_routes = Blueprint('servers', __name__)
private_server_routes = Blueprint('private_servers', __name__)

# GET all routes
@server_routes.route('/')
@login_required
def servers():
    servers = Server.query.all()
    return {'servers': [server.to_dict() for server in servers]}


@private_server_routes.route('/')
@login_required
def private_servers():

    private_servers = PrivateServer.query.all()
    return {'servers': [private_server.to_dict() for private_server in private_servers]}

# GET by Id routes
@server_routes.route('/<int:id>')
@login_required
def server(id):
    server = Server.query.get(id)
    return server.to_dict()


@private_server_routes.route('/<int:id>')
@login_required
def private_server(id):
    private_server = PrivateServer.query.get(id)
    return private_server.to_dict()


# POST a server
@server_routes.route('/', methods=['POST'])
@login_required
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
      channels=[Channel(
          name='welcome-test',
          topic="test topic 1",
          server_id=0,
          messages=[]
      )],
      serverInviteKey = generate_password_hash(f"{form.data['name']}")[-7:-1].upper(),
      ownerId = current_user.id
    )
    user = User.query.get(server.ownerId)
    db.session.add(server)
    user.serverList.append(server)
    db.session.commit()
    return server.to_dict()
  else:
    # print(form.errors)
    return "Bad data"


# POST a private_server
# @private_server_routes.route('/', methods=['POST'])
# def private_server_post():
#   pass

# PUT edit server
@server_routes.route('/edit/<int:id>', methods=['PUT'])
@login_required
def servers_edit(id):
  server_edit = Server.query.get_or_404(id)
  form = ServerForm()
  form['csrf_token'].data = request.cookies['csrf_token']

  if form.validate_on_submit():
    server_edit.name = form.data['name'],
    server_edit.description = form.data['description'],
    server_edit.serverImg = form.data['serverImg']
  try:
    db.session.commit()
    return server_edit.to_dict()
  except:
    # print(form.errors)
    return "Bad data"


@server_routes.route('/delete/<int:id>', methods=['DELETE'])
@login_required
def server_delete(id):
  server = Server.query.filter(Server.id == id).first()
  try:
    db.session.delete(server)
    db.session.commit()
    return server.to_dict()
  except:
    return "No Server Found"
