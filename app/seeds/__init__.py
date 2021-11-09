from flask.cli import AppGroup
from .users import seed_users, undo_users
from .servers import seed_servers, undo_servers
from .set_relationships import set_relationsips
# from .messages import seed_messages, undo_messages


# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    seed_users()
    seed_servers()
    # seed_messages()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_users()
    undo_servers()
    # undo_messages()
    # Add other undo functions here

@seed_commands.command('set')
def set():
    set_relationsips()
        # undo_messages()
        # Add other undo functions here
