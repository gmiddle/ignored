from flask import Blueprint, redirect, request
from flask_login import login_required
from app.forms import NewChannelForm, NewPrivateChannelForm
from app.models import db, Channel, PrivateChannel, Server

channel_routes = Blueprint('channels', __name__)
private_channel_routes = Blueprint('private_channels', __name__)


# GET all routes
@channel_routes.route('/')
@login_required
def channels():
    channels = Channel.query.all()
    return {'channels': [channel.to_dict() for channel in channels]}


@private_channel_routes.route('/')
@login_required
def private_channels():
    private_channels = PrivateChannel.query.all()
    return {'channels': [private_channel.to_dict() for private_channel in private_channels]}


# GET by Id routes
@channel_routes.route('/<int:id>')
@login_required
def channel(id):
    channel = Channel.query.get(id)
    return channel.to_dict()


@private_channel_routes.route('/<int:id>')
@login_required
def private_channel(id):
    private_channel = PrivateChannel.query.get(id)
    return private_channel.to_dict()


# POST add a new channel
@channel_routes.route("server/<int:id>/new", methods=['POST'])
@login_required
def new_channel_form(id):

    form = NewChannelForm()

    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
      data = form.data
      usernames = []

      new_channel = Channel(name=data["name"],
                            topic=data["topic"],
                            server_id=id,
                            messages = []
                            )
      server = Server.query.get(int(id))
      db.session.add(new_channel)
      server.channels.append(new_channel)
      db.session.commit()
      return new_channel.to_dict()
    else:
    # print(form.errors)
      return "Bad Data"


@private_channel_routes.route("/new", methods=['POST'])
@login_required
def new_private_channel_form():
    form = NewPrivateChannelForm()
    if form.validate_on_submit():
        data = form.data
        new_private_channel = PrivateChannel(name=data["name"],
                              topic=data["topic"],
                              server_id=request.args.get('server_id'),
                              messages = []
                              )
        db.session.add(new_private_channel)
        db.session.commit()
        return redirect(f'/server/{new_private_channel.server_id}/')
    else:
            # print(form.errors)
            return "Bad Data"


# PUT edit an existing channel
@channel_routes.route("/edit/<int:id>", methods=['PUT'])
@login_required
def channel_edit(id):
    channel_to_edit = Channel.query.get_or_404(id)
    form = NewChannelForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        channel_to_edit.name = form.data['name']
        channel_to_edit.topic = form.data['topic']
    try:
        db.session.commit()
        return channel_to_edit.to_dict()
    except:
        return "Channel not found, could not edit"


@private_channel_routes.route("/private/edit/<int:id>", methods=['PUT'])
@login_required
def private_channel_edit(id):
    private_channel_to_edit = PrivateChannel.query.get_or_404(id)
    form = NewPrivateChannelForm()
    if form.validate_on_submit():
        private_channel_to_edit.name = request.form['name']
        private_channel_to_edit.topic = request.form['topic']
    try:
        db.session.commit()
        return redirect('')
    except:
        return "Channel not found, could not edit"

# DELETE remove an existing channel
@channel_routes.route("/delete/<int:id>", methods=['DELETE'])
@login_required
def channel_delete(id):
   
    channel_to_delete = Channel.query.filter(Channel.id == id).first()

    try:
        db.session.delete(channel_to_delete)
        db.session.commit()
        return channel_to_delete.to_dict()
    except:
        return "Channel not found, could not delete"


@private_channel_routes.route("/delete/<int:id>", methods=['DELETE'])
@login_required
def private_channel_delete(id):
    private_channel_to_delete = PrivateChannel.query.get_or_404(id)

    try:
        db.session.delete(private_channel_to_delete)
        db.session.commit()
        return
    except:
        return "Channel not found, could not delete"
