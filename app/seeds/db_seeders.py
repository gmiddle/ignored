from app.models import db, Server, Channel, Message, PrivateServer, PrivateChannel, PrivateMessage 
from werkzeug.security import generate_password_hash
from faker import Faker
import random
import datetime as dt

fake = Faker()

total_users = 30
total_servers = 20

def seed_server():
    demo_server1 = Server(
        name='Demo Server',
        description='This is a demo server',
        ownerId=1,
        serverImg='',
        serverInviteKey=generate_password_hash('Demo Server')[-7:-1].upper(),
        channels=[],
    )

    demo_server2 = Server(
        name='demoServer2', 
        description='A demo server for endpoint testing', 
        ownerId=1, 
        serverImg='', 
        serverInviteKey=generate_password_hash('t')[-7:-1].upper(), 
        channels=[],
    )

    demo_server3 = Server(
        name='demoServer3', 
        description='A demo server for endpoint testing', 
        ownerId=2, 
        serverImg='', 
        serverInviteKey=generate_password_hash('t')[-7:-1].upper(), 
        channels=[]
    )

    db.session.add(demo_server1)
    db.session.add(demo_server2)
    db.session.add(demo_server3)

    # server_adjectives =[
    #     'Hangout',
    #     'Favorite Server',
    #     'Secret Hideout'
    # ]

    server_names =[
        'Hangout',
        'Favorite Server',
        'Secret Hideout'
    ]

    for server in server_names:
        new_server = Server(
            name=server,
            description='A demo server for endpoint testing',
            ownerId=random.randint(1,3),
            serverImg='',
            serverInviteKey=generate_password_hash(server)[-7:-1].upper(),
            channels=[]
        )
        db.session.add(new_server)
    db.session.commit()


def seed_private_server():
    demo_private_server1 = PrivateServer(
        name='Demo Server',
        description='This is a demo private server for user 1',
        serverImg='',
        serverInviteKey= generate_password_hash('Demo Server')[-7:-1].upper(),
        private_channels=[]
    )


    demo_private_server2 = PrivateServer(
        name='demoServer2', 
        description='A demo private server for user 2', 
        serverImg='',
        serverInviteKey= generate_password_hash('Demo Server3')[-7:-1].upper(),
        private_channels=[]
    )

    demo_private_server3 = PrivateServer(
        name='demoPrivateServer3', 
        description='A demo private server for user 3', 
        serverImg='',
        serverInviteKey= generate_password_hash('Demo Server2')[-7:-1].upper(),
        private_channels=[]
    )

    db.session.add(demo_private_server1)
    db.session.add(demo_private_server2)
    db.session.add(demo_private_server3)
    # for server in range(1, total_servers + 1):
    #     users = []
    #     for _ in range(1, 11):
    #         while True:
    #             user = random.randint(1, total_users)
    #             if user not in users:
    #                 new_private_server = PrivateServer(
    #                     server_id=server,
    #                     user_id=user
    #                 )
    #                 db.session.add(new_private_server)
    #                 users.append(user)
    #                 break
    db.session.commit()


def seed_channel():
    base_channels = [
        'welcome',
        'announcements',
        'general',
        'lounge',
        'notes',
        'resources',
        'music',
        'the-memes',
    ]
    for channel in base_channels:
        demo_channel = Channel(
            name=channel,
            topic="test topic",
            server_id=1,
            messages=[]
        )
        db.session.add(demo_channel)
    
    for channel in base_channels:
        demo_channel = Channel(
            name=channel,
            topic="test topic",
            server_id=2,
            messages=[]
        )
        db.session.add(demo_channel)
    
    for channel in base_channels:
        demo_channel = Channel(
            name=channel,
            topic="test topic",
            server_id=3,
            messages=[]
        )
        db.session.add(demo_channel)
    
    for channel in base_channels:
        demo_channel = Channel(
            name=channel,
            topic="test topic",
            server_id=4,
            messages=[]
        )
        db.session.add(demo_channel)
    
    for channel in base_channels:
        demo_channel = Channel(
            name=channel,
            topic="test topic",
            server_id=5,
            messages=[]
        )
        db.session.add(demo_channel)
    
    for channel in base_channels:
        demo_channel = Channel(
            name=channel,
            topic="test topic",
            server_id=5,
            messages=[]
        )
        db.session.add(demo_channel)
    
    for channel in base_channels:
        demo_channel = Channel(
            name=channel,
            topic="test topic",
            server_id=6,
            messages=[]
        )
        db.session.add(demo_channel)
    
    # random_channel_names = [
    #     'art',
    #     'anime',
    #     'exercise',
    #     'movies',
    #     'tv-shows',
    #     'pet-pictures',
    #     'video-games',
    #     'office-talk',
    #     'the-yoke',
    #     'networking',
    #     'projects',
    #     'homework-help'
    #     'study-session-planning',
    #     'social-media',
    #     'wows-only-channel',
    #     'arts-and-crafts',
    #     'gamer-talk',
    #     'off-topic',
    #     'cooking-and-recipes'
    # ]
    # for i in range(1, total_servers + 1):
    #     current_channels = base_channels
        
    #     for channel in current_channels:
    #         base_channel = Channel(
    #             name=channel,
    #             server_id=i
    #         )
    #         db.session.add(base_channel)

    #     for _ in range(1, 7):
    #         while True:
    #             channel_name = random_channel_names[random.randint(1, len(random_channel_names)-1)]
    #             if channel_name not in current_channels:
    #                 current_channels.append(channel_name)
    #                 new_channel = Channel(
    #                     name=channel_name,
    #                     server_id=i
    #                 )
    #                 break
    #         db.session.add(new_channel)
    db.session.commit()


def seed_private_channel():
    private_channel1 = PrivateChannel(
        name='Demo Channel',
        topic='This is a demo private channel for server 1',
        private_server_id=3,
        private_messages=[]
    )

    private_channel2 = PrivateChannel(
        name='demoChannel2', 
        topic='A demo private channel for server 2', 
        private_server_id=3,
        private_messages=[]
    )

    private_channel3 = PrivateChannel(
        name='demoPrivateChannel3', 
        topic='A demo private channel for server 3', 
        private_server_id=3,
        private_messages=[]
    )

    db.session.add(private_channel1)
    db.session.add(private_channel2)
    db.session.add(private_channel3)


def seed_message():
    for i in range(0, 200):
        new_message = Message(
            content=f'This is test message # {i}',
            channel_id=random.randint(1, total_users + 1),
            user_id=random.randint(1, total_users + 1),
            # sent_date=dt.datetime.now()
        )
        db.session.add(new_message)
    db.session.commit()


def seed_private_message():
    for i in range(0, 200):
        new_message = PrivateMessage(
            content=f'This is test private message # {i}',
            channel_id=random.randint(1, total_users + 1),
            user_id=random.randint(1, total_users + 1),
            # sent_date=dt.datetime.now()
        )
        db.session.add(new_message)
    db.session.commit()


def seed_all():
    seed_server()
    seed_private_server()
    seed_channel()
    seed_private_channel()
    seed_message()
    seed_private_message()


def undo_all():
    db.session.execute(f'TRUNCATE Message RESTART IDENTITY CASCADE;')
    db.session.commit()
    db.session.execute(f'TRUNCATE PrivateMessage RESTART IDENTITY CASCADE;')
    db.session.commit()
    db.session.execute(f'TRUNCATE Channel RESTART IDENTITY CASCADE;')
    db.session.commit()
    db.session.execute(f'TRUNCATE PrivateServer RESTART IDENTITY CASCADE;')
    db.session.commit()
    db.session.execute(f'TRUNCATE Server RESTART IDENTITY CASCADE;')
    db.session.commit()
    # db.session.execute(f'TRUNCATE User RESTART IDENTITY CASCADE;')
    # db.session.commit()



# if __name__ == '__main__':
#     seed_all()

