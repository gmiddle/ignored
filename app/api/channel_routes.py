from flask import Blueprint, jsonify, redirect, request
from flask_login import login_required
from app.forms import NewChannelForm, NewPrivateChannelForm
from app.models import db, Channel, PrivateChannel

channel_routes = Blueprint('channels', __name__)
private_channel_routes = Blueprint('private_channels', __name__)


# GET all routes
@channel_routes.route('/')
def channels():
    channels = Channel.query.all()
    return {'channels': [channel.to_dict() for channel in channels]}


@private_channel_routes.route('/')
def private_channels():
    private_channels = PrivateChannel.query.all()
    return {'channels': [private_channel.to_dict() for private_channel in private_channels]}

# GET by Id routes
@channel_routes.route('/<int:id>')
def channel(id):
    channel = Channel.query.get(id)
    return channel.to_dict()


@private_channel_routes.route('/<int:id>')
def private_channel(id):
    private_channel = PrivateChannel.query.get(id)
    return private_channel.to_dict()


# POST add a new channel
@channel_routes.route("/new", methods=['POST'])
def new_channel_form():
    form = NewChannelForm()
    if form.validate_on_submit():
        data = form.data
        usernames = []
        new_channel = Channel(name=data["name"],
                              topic=data["topic"],
                              server_id=request.args.get('server_id'),
                              messages = []
                              )
        db.session.add(new_channel)
        db.session.commit()
        return redirect(f'/server/{new_channel.server_id}/')
    else:
            print(form.errors)
            return "Bad Data"


@private_channel_routes.route("/new", methods=['POST'])
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
            print(form.errors)
            return "Bad Data"

# PUT edit an existing channel
@channel_routes.route("/edit/<int:id>", methods=['PUT'])
def channel_edit(id):
    channel_to_edit = Channel.query.get_or_404(id)
    form = NewChannelForm()
    if form.validate_on_submit():
        channel_to_edit.name = request.form['name']
        channel_to_edit.topic = request.form['topic']
    try:
        db.session.commit()
        return redirect('')
    except:
        return "Channel not found, could not edit"



# PUT edit an existing channel
@channel_routes.route("/edit/<int:id>", methods=['PUT'])
def channel_edit(id):
    channel_to_edit = Channel.query.get_or_404(id)
    form = NewChannelForm()
    if form.validate_on_submit():
        channel_to_edit.name = request.form['name']
        channel_to_edit.topic = request.form['topic']
    try:
        db.session.commit()
        return redirect('')
    except:
        return "Channel not found, could not edit"


@private_channel_routes.route("/edit/<int:id>", methods=['PUT'])
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

# DELETE remove an exisiting channel
@channel_routes.route("/delete/<int:id>", methods=['DELETE'])
def channel_delete(id):
    channel_to_delete = Channel.query.get_or_404(id)

    try:
        db.session.delete(channel_to_delete)
        db.session.commit()
        return redirect('')
    except:
        return "Channel not found, could not delete"


@private_channel_routes.route("/delete/<int:id>", methods=['DELETE'])
def private_channel_delete(id):
    private_channel_to_delete = PrivateChannel.query.get_or_404(id)

    try:
        db.session.delete(private_channel_to_delete)
        db.session.commit()
        return redirect('')
    except:
        return "Channel not found, could not delete"
