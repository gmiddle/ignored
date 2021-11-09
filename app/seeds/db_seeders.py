from app.models import db, Server, Channel, Message, PrivateServer, PrivateChannel, PrivateMessage 
from werkzeug.security import generate_password_hash
from faker import Faker
import random
import datetime as dt

fake = Faker()

total_users = 30
total_servers = 20

def seed_server():
    demo_server = Server(
        name='Demo Server',
        description='This is a demo server',
        serverImg='',
        serverInviteKey=generate_password_hash('Demo Server')[-7:-1].upper(),
        channels='',
        # owner_id=1,
    )
    db.session.add(demo_server)

    server_adjectives =[
        'Hangout',
        'Favorite Server',
        'Secret Hideout'
    ]

    for _ in range(0, 30):
        user = fake.username()
        server_name = f'{user}\'s {server_adjectives[random.radint(1, len(server_adjectives) + 1)]}'
        new_server = Server(
            name=server_name,
            serverImg='',
            serverInviteKey=generate_password_hash(server_name)[-7:-1].upper()
        )
        db.session.add(new_server)
    db.session.commit()


def seed_private_server():
    for server in range(1, total_servers + 1):
        users = []
        for _ in range(1, 11):
            while True:
                user = random.randint(1, total_users)
                if user not in users:
                    new_private_server = PrivateServer(
                        server_id=server,
                        user_id=user
                    )
                    db.session.add(new_private_server)
                    users.append(user)
                    break
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
            server_id=1
        )
        db.session.add(demo_channel)
    
    random_channel_names = [
        'art',
        'anime',
        'exercise',
        'movies',
        'tv-shows',
        'pet-pictures',
        'video-games',
        'office-talk',
        'the-yoke',
        'networking',
        'projects',
        'homework-help'
        'study-session-planning',
        'social-media',
        'wows-only-channel',
        'arts-and-crafts',
        'gamer-talk',
        'off-topic',
        'cooking-and-recipes'
    ]
    for i in range(1, total_servers + 1):
        current_channels = base_channels
        
        for channel in current_channels:
            base_channel = Channel(
                name=channel,
                server_id=i
            )
            db.session.add(base_channel)

        for _ in range(1, 7):
            while True:
                channel_name = random_channel_names[random.randint(1, len(random_channel_names)-1)]
                if channel_name not in current_channels:
                    current_channels.append(channel_name)
                    new_channel = Channel(
                        name=channel_name,
                        server_id=i
                    )
                    break
            db.session.add(new_channel)
    db.session.commit()


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
    db.session.execute(f'TRUNCATE User RESTART IDENTITY CASCADE;')
    db.session.commit()



# if __name__ == '__main__':
#     seed_all()

