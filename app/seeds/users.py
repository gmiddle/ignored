from app.models import db, User, Server, Channel, Message, PrivateServer, PrivateChannel, PrivateMessage, private_channel
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
            name="Demo's First Server",
            description='Description of server',
            ownerId=1,
            serverImg='https://res.cloudinary.com/dxo7djnid/image/upload/v1636757375/ignored/discord_server_icons/minecraft_discord_server_icon_nsp4a4.png',
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
            name="Demo's Second Server",
            description='Description of server',
            ownerId=1,
            serverImg='https://res.cloudinary.com/dxo7djnid/image/upload/v1636757375/ignored/discord_server_icons/minecraft_discord_server_icon_nsp4a4.png',
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
            name="Demo's Third Server",
            description='Description of server',
            ownerId=1,
            serverImg='https://res.cloudinary.com/dxo7djnid/image/upload/v1636757375/ignored/discord_server_icons/minecraft_discord_server_icon_nsp4a4.png',
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
            name="Demo's Fourth Server",
            description='Description of server',
            ownerId=1,
            serverImg='https://res.cloudinary.com/dxo7djnid/image/upload/v1636757375/ignored/discord_server_icons/minecraft_discord_server_icon_nsp4a4.png',
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
        privateServerList=[
            PrivateServer(
                name='Home - Demo',
                description='Demo User Home / Private Server',
                serverImg='https://res.cloudinary.com/dxo7djnid/image/upload/v1636757202/ignored/discord_server_icons/regular_discord_server_icon_yctjzy.png',
                serverInviteKey=generate_password_hash(f'{random.randint(1,10000)}')[-7:-1].upper(),
                ownerId=1,
                private_channels=[
                    PrivateChannel(
                    name="Demo's Private Channel",
                    topic="test topic 1",
                    private_server_id=1,
                    private_messages=[
                        PrivateMessage(
                            content='Demo Home - This is a private test message 1',
                            channel_id=1,
                            user_id=random.randint(1,3),
                        ),
                        PrivateMessage(
                            content='Demo Home - This is a private test message 2',
                            channel_id=1,
                            user_id=random.randint(1,3),
                        ),
                        PrivateMessage(
                            content='Demo Home - This is a private test message 3',
                            channel_id=1,
                            user_id=random.randint(1,3)
                        )
                    ])
                ]
            )
        ],
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
            name="Marnie's First Server",
            description='Description of server',
            ownerId=2,
            serverImg='https://res.cloudinary.com/dxo7djnid/image/upload/v1636757375/ignored/discord_server_icons/minecraft_discord_server_icon_nsp4a4.png',
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
            name="Marnie's Second Server",
            description='Description of server',
            ownerId=2,
            serverImg='https://res.cloudinary.com/dxo7djnid/image/upload/v1636757375/ignored/discord_server_icons/minecraft_discord_server_icon_nsp4a4.png',
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
            name="Marnie's Third Server",
            description='Description of server',
            ownerId=2,
            serverImg='https://res.cloudinary.com/dxo7djnid/image/upload/v1636757375/ignored/discord_server_icons/minecraft_discord_server_icon_nsp4a4.png',
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
        ],
        privateServerList=[
            PrivateServer(
                name='Home - Marnie',
                description='Marnie Home / Private Server',
                serverImg='https://res.cloudinary.com/dxo7djnid/image/upload/v1636757202/ignored/discord_server_icons/regular_discord_server_icon_yctjzy.png',
                serverInviteKey=generate_password_hash(f'{random.randint(1,10000)}')[-7:-1].upper(),
                ownerId=2,
                private_channels=[
                    PrivateChannel(
                    name="Marnie's Private Channel",
                    topic="test topic 1",
                    private_server_id=1,
                    private_messages=[
                        PrivateMessage(
                            content='Marnie Home - This is a private test message 1',
                            channel_id=1,
                            user_id=random.randint(1,3),
                        ),
                        PrivateMessage(
                            content='Marnie Home - This is a private test message 2',
                            channel_id=1,
                            user_id=random.randint(1,3),
                        ),
                        PrivateMessage(
                            content='Marnie Home - This is a private test message 3',
                            channel_id=1,
                            user_id=random.randint(1,3)
                        )
                    ])
                ]
            )
        ],
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
            name="Bobbie's First Server",
            description='Description of server',
            ownerId=3,
            serverImg='https://res.cloudinary.com/dxo7djnid/image/upload/v1636757375/ignored/discord_server_icons/minecraft_discord_server_icon_nsp4a4.png',
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
            name="Bobbie's Second Server",
            description='Description of server',
            ownerId=3,
            serverImg='https://res.cloudinary.com/dxo7djnid/image/upload/v1636757375/ignored/discord_server_icons/minecraft_discord_server_icon_nsp4a4.png',
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
            name="Bobbie's Third Server",
            description='Description of server',
            ownerId=3,
            serverImg='https://res.cloudinary.com/dxo7djnid/image/upload/v1636757375/ignored/discord_server_icons/minecraft_discord_server_icon_nsp4a4.png',
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
        ],
        privateServerList=[
            PrivateServer(
                name='Home - Bobbie',
                description='Bobbie Home / Private Server',
                serverImg='https://res.cloudinary.com/dxo7djnid/image/upload/v1636757202/ignored/discord_server_icons/regular_discord_server_icon_yctjzy.png',
                serverInviteKey=generate_password_hash(f'{random.randint(1,10000)}')[-7:-1].upper(),
                ownerId=3,
                private_channels=[
                    PrivateChannel(
                    name="Bobbie's Private Channel",
                    topic="test topic 1",
                    private_server_id=1,
                    private_messages=[
                        PrivateMessage(
                            content="Bobbie Channel - Hey, what's up!",
                            channel_id=1,
                            user_id=random.randint(1,3),
                        ),
                        PrivateMessage(
                            content="Bobbie Channel - Not much!",
                            channel_id=1,
                            user_id=random.randint(1,3),
                        ),
                        PrivateMessage(
                            content="Bobbie Channel - Can't wait for tomorrow!",
                            channel_id=1,
                            user_id=random.randint(1,3)
                        )
                    ])
                ]
            )
        ],
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
