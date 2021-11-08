from app.models import db, Server, Channel, Message
from werkzeug.security import generate_password_hash, check_password_hash
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
        serverInviteKey=generate_password_hash('password')[0:9],
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
            serverInviteKey=generate_password_hash(server_name)[-8:]
        )
        db.session.add(new_server)
    db.session.commit()


def seed_user_server():
    for i in range(1, total_servers + 1):
        new_user_server = User_Server(
            serverId=i,
            userId=i
        )
        db.sessionadd(new_user_server)
    db.session.commit()


def seed_friends():
    for i in range(1, total_users - 1):
        new_user_server = Friend(
            sender_userId=i,
            rec_userId=i
        )
        db.session.add(new_user_server)
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


def seed_all():
    seed_server()
    seed_user_server()
    seed_channel()
    seed_message()
    seed_friends()


def undo_all():
    models = [
        Server, Channel, Message,
        # User_Server
    ]
    for model in models:
        db.session.execute(f'TRUNCATE {model} RESTART IDENTITY CASCADE;')
        db.session.commit()


# if __name__ == '__main__':
#     seed_all()
#     # undo_all()
