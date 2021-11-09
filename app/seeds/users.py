from app.models import db, User, Server, Channel, Message
from werkzeug.security import generate_password_hash


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        username='demo',
        email='demo@aa.io',
        password='password',
        serverList=[
            Server(
            name='Demo Server',
            description='This is a demo server',
            ownerId=1,
            serverImg='',
            serverInviteKey=generate_password_hash('Demo Server')[-7:-1].upper(),
            channels=[
                Channel(
                name="Channel 1",
                topic="test topic 1",
                server_id=1,
                messages=[
                    Message(
                        content='This is test message',
                        channel_id=1,
                        user_id=1,
                    ),
                ]
                )
            ]
            ),
            Server(
            name='Demo Server2',
            description='This is a demo server',
            ownerId=1,
            serverImg='',
            serverInviteKey=generate_password_hash('Demo Server2')[-7:-1].upper(),
            channels=[
                Channel(
                name="Channel wahoo",
                topic="test topic 2",
                server_id=2,
                messages=[
                    Message(
                        content='This is test message 2',
                        channel_id=2,
                        user_id=1,
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
            name='Demo Server4',
            description='This is a demo server',
            ownerId=2,
            serverImg='',
            serverInviteKey=generate_password_hash('Demo Server')[-7:-1].upper(),
            channels=[
                Channel(
                name="Channel special",
                topic="test topic 1",
                server_id=4,
                messages=[
                    Message(
                        content='I should be Marnie and I should own this server',
                        channel_id=4,
                        user_id=2,
                    ),
                ]
                )
            ]
            ),
            Server(
            name='Demo Server5',
            description='This is a demo server',
            ownerId=2,
            serverImg='',
            serverInviteKey=generate_password_hash('Demo Server2')[-7:-1].upper(),
            channels=[
                Channel(
                name="Channel 2",
                topic="test topic 2",
                server_id=5,
                messages=[
                    Message(
                        content='I should be Marnie and I should own this server',
                        channel_id=5,
                        user_id=2,
                    ),
                ]
                )
            ]
            ),Server(
            name='Demo Server6',
            description='This is a demo server',
            ownerId=2,
            serverImg='',
            serverInviteKey=generate_password_hash('Demo Server2')[-7:-1].upper(),
            channels=[
                Channel(
                name="Channel 6",
                topic="test topic 6",
                server_id=6,
                messages=[
                    Message(
                        content='I should be demo user and I should own this server',
                        channel_id=6,
                        user_id=1,
                    ),
                ]
                )
            ]
            )
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
        serverList=[Server(
            name='Demo Server7',
            description='This is a demo server',
            ownerId=3,
            serverImg='',
            serverInviteKey=generate_password_hash('Demo Server2')[-7:-1].upper(),
            channels=[
                Channel(
                name="Channel 7",
                topic="test topic 7",
                server_id=7,
                messages=[
                    Message(
                        content='I should be Marnie, this server is owned by bobbie',
                        channel_id=7,
                        user_id=2,
                    ),
                ]
                )
            ]
            ),Server(
            name='Demo Server8',
            description='This is a demo server',
            ownerId=2,
            serverImg='',
            serverInviteKey=generate_password_hash('Demo Server2')[-7:-1].upper(),
            channels=[
                Channel(
                name="Channel 8",
                topic="test topic 8",
                server_id=8,
                messages=[
                    Message(
                        content='I am Marnie and I own this server',
                        channel_id=8,
                        user_id=2,
                    ),
                ]
                )
            ]
            ),Server(
            name='Demo Server9',
            description='This is a demo server',
            ownerId=1,
            serverImg='',
            serverInviteKey=generate_password_hash('Demo Server2')[-7:-1].upper(),
            channels=[
                Channel(
                name="Channel 9",
                topic="test topic 9",
                server_id=9,
                messages=[
                    Message(
                        content='I should be Demo and I should own this server',
                        channel_id=9,
                        user_id=1,
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
