from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from app.forms import ServerForm
from app.models import Server, PrivateServer

server_routes = Blueprint('servers', __name__)
private_server_routes = Blueprint('private_servers', __name__)
# GET all routes
@server_routes.route('/')
def servers():
    servers = Server.query.all()
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
@server_routes.route('/', mehtods=['POST'])
def servers_post():
  """
  Creates a new server
  """
  form = ServerForm()

# POST a private_server
@private_server_routes.route('/', methods=['POST'])
def private_server_post():
  pass
