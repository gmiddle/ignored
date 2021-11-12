from app.models import db, User, Server, Channel, Message
from werkzeug.security import generate_password_hash
from faker import Faker
import random

fake = Faker()



# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        username='demo',
        email='demo@aa.io',
        password='password',
        profilePic="",
        serverList=[
            Server(
            name=f'{fake.name()}\'s Server',
            description='Description of server',
            ownerId=1,
            serverImg='',
            serverInviteKey=generate_password_hash(f'{random.randint(1,10000)}')[-7:-1].upper(),
            channels=[
                Channel(
                name='welcome1',
                topic="test topic 1",
                server_id=1,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                ),
                Channel(
                name='general',
                topic="test topic 1",
                server_id=2,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                ),
                Channel(
                name='lounge',
                topic="test topic 1",
                server_id=3,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                ),

                Channel(
                name='resources',
                topic="test topic 1",
                server_id=4,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                ),
                Channel(
                name='the-memes',
                topic="test topic 1",
                server_id=5,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                )
            ]
            ),
            Server(
            name=f'{fake.name()}\'s Server',
            description='Description of server',
            ownerId=1,
            serverImg='',
            serverInviteKey=generate_password_hash(f'{random.randint(1,10000)}')[-7:-1].upper(),
            channels=[
                Channel(
                name='welcome2',
                topic="test topic 1",
                server_id=1,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                ),
                Channel(
                name='general',
                topic="test topic 1",
                server_id=2,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                ),
                Channel(
                name='lounge',
                topic="test topic 1",
                server_id=3,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                ),
                Channel(
                name='resources',
                topic="test topic 1",
                server_id=4,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                ),
                Channel(
                name='the-memes',
                topic="test topic 1",
                server_id=5,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                )
            ]
            ),
            Server(
            name=f'{fake.name()}\'s Server',
            description='Description of server',
            ownerId=1,
            serverImg='',
            serverInviteKey=generate_password_hash(f'{random.randint(1,10000)}')[-7:-1].upper(),
            channels=[
                Channel(
                name='welcome3',
                topic="test topic 1",
                server_id=1,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                ),
                Channel(
                name='general',
                topic="test topic 1",
                server_id=2,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                ),
                Channel(
                name='lounge',
                topic="test topic 1",
                server_id=3,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                ),
                Channel(
                name='resources',
                topic="test topic 1",
                server_id=4,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                ),
                Channel(
                name='the-memes',
                topic="test topic 1",
                server_id=5,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                )
            ]
            ),
            Server(
            name=f'{fake.name()}\'s Server',
            description='Description of server',
            ownerId=1,
            serverImg='',
            serverInviteKey=generate_password_hash(f'{random.randint(1,10000)}')[-7:-1].upper(),
            channels=[
                Channel(
                name='welcome4',
                topic="test topic 1",
                server_id=1,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                ),
                Channel(
                name='general',
                topic="test topic 1",
                server_id=2,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                ),
                Channel(
                name='lounge',
                topic="test topic 1",
                server_id=3,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                ),
                Channel(
                name='resources',
                topic="test topic 1",
                server_id=4,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                ),
                Channel(
                name='the-memes',
                topic="test topic 1",
                server_id=5,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                )
            ]
            ),
        ],
        privateServerList=[],
        messages=[],
        private_messages=[],
        friendships=[]
    )


    marnie = User(
        username='marnie',
        email='marnie@aa.io',
        password='password',
        serverList=[
            Server(
            name=f'{fake.name()}\'s Server',
            description='Description of server',
            ownerId=2,
            serverImg='',
            serverInviteKey=generate_password_hash(f'{random.randint(1,10000)}')[-7:-1].upper(),
            channels=[
                Channel(
                name='welcome5',
                topic="test topic 1",
                server_id=1,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                ),
                Channel(
                name='general',
                topic="test topic 1",
                server_id=2,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                ),
                Channel(
                name='lounge',
                topic="test topic 1",
                server_id=3,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                ),
                Channel(
                name='resources',
                topic="test topic 1",
                server_id=4,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                ),
                Channel(
                name='the-memes',
                topic="test topic 1",
                server_id=5,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                )
            ]
            ),
            Server(
            name=f'{fake.name()}\'s Server',
            description='Description of server',
            ownerId=2,
            serverImg='',
            serverInviteKey=generate_password_hash(f'{random.randint(1,10000)}')[-7:-1].upper(),
            channels=[
                Channel(
                name='welcome6',
                topic="test topic 1",
                server_id=1,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                ),
                Channel(
                name='general',
                topic="test topic 1",
                server_id=2,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                ),
                Channel(
                name='lounge',
                topic="test topic 1",
                server_id=3,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                ),
                Channel(
                name='resources',
                topic="test topic 1",
                server_id=4,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                ),
                Channel(
                name='the-memes',
                topic="test topic 1",
                server_id=5,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                )
            ]
            ),
            Server(
            name=f'{fake.name()}\'s Server',
            description='Description of server',
            ownerId=2,
            serverImg='',
            serverInviteKey=generate_password_hash(f'{random.randint(1,10000)}')[-7:-1].upper(),
            channels=[
                Channel(
                name='welcome7',
                topic="test topic 1",
                server_id=1,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                ),
                Channel(
                name='general',
                topic="test topic 1",
                server_id=2,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                ),
                Channel(
                name='lounge',
                topic="test topic 1",
                server_id=3,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                ),
                Channel(
                name='resources',
                topic="test topic 1",
                server_id=4,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                ),
                Channel(
                name='the-memes',
                topic="test topic 1",
                server_id=5,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                )
            ]
            ),
            Server(
            name=f'{fake.name()}\'s Server',
            description='Description of server',
            ownerId=2,
            serverImg='',
            serverInviteKey=generate_password_hash(f'{random.randint(1,10000)}')[-7:-1].upper(),
            channels=[
                Channel(
                name='welcome8',
                topic="test topic 1",
                server_id=1,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                ),
                Channel(
                name='general',
                topic="test topic 1",
                server_id=2,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                ),
                Channel(
                name='lounge',
                topic="test topic 1",
                server_id=3,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                ),
                Channel(
                name='resources',
                topic="test topic 1",
                server_id=4,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                ),
                Channel(
                name='the-memes',
                topic="test topic 1",
                server_id=5,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                )
            ]
            ),
            Server(
            name=f'{fake.name()}\'s Server',
            description='Description of server',
            ownerId=2,
            serverImg='',
            serverInviteKey=generate_password_hash(f'{random.randint(1,10000)}')[-7:-1].upper(),
            channels=[
                Channel(
                name='welcome9',
                topic="test topic 1",
                server_id=1,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                ),
                Channel(
                name='general',
                topic="test topic 1",
                server_id=2,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                ),
                Channel(
                name='lounge',
                topic="test topic 1",
                server_id=3,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                ),
                Channel(
                name='resources',
                topic="test topic 1",
                server_id=4,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                ),
                Channel(
                name='the-memes',
                topic="test topic 1",
                server_id=5,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                )
            ]
            ),
        ],
        privateServerList=[],
        messages=[],
        private_messages=[],
        friendships=[]
    )

    bobbie = User(
        username='bobbie',
        email='bobbie@aa.io',
        password='password',
        serverList=[
            Server(
            name=f'{fake.name()}\'s Server',
            description='Description of server',
            ownerId=3,
            serverImg='',
            serverInviteKey=generate_password_hash(f'{random.randint(1,10000)}')[-7:-1].upper(),
            channels=[
                Channel(
                name='welcome10',
                topic="test topic 1",
                server_id=1,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=2,
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=3,
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=2,
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=3,
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                ),
                Channel(
                name='general',
                topic="test topic 1",
                server_id=2,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                ),
                Channel(
                name='lounge',
                topic="test topic 1",
                server_id=3,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                ),
                Channel(
                name='resources',
                topic="test topic 1",
                server_id=4,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                ),
                Channel(
                name='the-memes',
                topic="test topic 1",
                server_id=5,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                )
            ]
            ),
            Server(
            name=f'{fake.name()}\'s Server',
            description='Description of server',
            ownerId=3,
            serverImg='',
            serverInviteKey=generate_password_hash(f'{random.randint(1,10000)}')[-7:-1].upper(),
            channels=[
                Channel(
                name='welcome11',
                topic="test topic 1",
                server_id=1,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                ),
                Channel(
                name='general',
                topic="test topic 1",
                server_id=2,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                ),
                Channel(
                name='lounge',
                topic="test topic 1",
                server_id=3,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                ),
                Channel(
                name='resources',
                topic="test topic 1",
                server_id=4,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                ),
                Channel(
                name='the-memes',
                topic="test topic 1",
                server_id=5,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                )
            ]
            ),
            Server(
            name=f'{fake.name()}\'s Server',
            description='Description of server',
            ownerId=3,
            serverImg='',
            serverInviteKey=generate_password_hash(f'{random.randint(1,10000)}')[-7:-1].upper(),
            channels=[
                Channel(
                name='welcome12',
                topic="test topic 1",
                server_id=1,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                ),
                Channel(
                name='general',
                topic="test topic 1",
                server_id=2,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                ),
                Channel(
                name='lounge',
                topic="test topic 1",
                server_id=3,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                ),
                Channel(
                name='resources',
                topic="test topic 1",
                server_id=4,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                ),
                Channel(
                name='the-memes',
                topic="test topic 1",
                server_id=5,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                )
            ]
            ),
            Server(
            name=f'{fake.name()}\'s Server',
            description='Description of server',
            ownerId=3,
            serverImg='',
            serverInviteKey=generate_password_hash(f'{random.randint(1,10000)}')[-7:-1].upper(),
            channels=[
                Channel(
                name='welcome13',
                topic="test topic 1",
                server_id=1,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                ),
                Channel(
                name='general',
                topic="test topic 1",
                server_id=2,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                ),
                Channel(
                name='lounge',
                topic="test topic 1",
                server_id=3,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                ),
                Channel(
                name='resources',
                topic="test topic 1",
                server_id=4,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                ),
                Channel(
                name='the-memes',
                topic="test topic 1",
                server_id=5,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                )
            ]
            ),
            Server(
            name=f'{fake.name()}\'s Server',
            description='Description of server',
            ownerId=3,
            serverImg='',
            serverInviteKey=generate_password_hash(f'{random.randint(1,10000)}')[-7:-1].upper(),
            channels=[
                Channel(
                name='welcome14',
                topic="test topic 1",
                server_id=1,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                ),
                Channel(
                name='general',
                topic="test topic 1",
                server_id=2,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                ),
                Channel(
                name='lounge',
                topic="test topic 1",
                server_id=3,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                ),
                Channel(
                name='resources',
                topic="test topic 1",
                server_id=4,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                ),
                Channel(
                name='the-memes',
                topic="test topic 1",
                server_id=5,
                messages=[
                    Message(
                        content='This is test message 1',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 2',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 3',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 4',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 5',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                    Message(
                        content='This is test message 6',
                        channel_id=1,
                        user_id=random.randint(1,3),
                    ),
                ]
                )
            ]
            ),
        ],
        privateServerList=[],
        messages=[],
        private_messages=[],
        friendships=[]
    )

    db.session.add(demo)
    db.session.add(marnie)
    db.session.add(bobbie)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_users():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()
