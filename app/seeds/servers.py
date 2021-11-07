from app.models import db, Server


# Adds a demo user, you can add other users here if you want
def seed_servers():
    demoServer1 = Server(
        name='demoServer1', description='A demo server for endpoint testing', serverImg='', serverInviteKey='server1key', channels=[])
    demoServer2 = Server(
        name='demoServer2', description='A demo server for endpoint testing', serverImg='', serverInviteKey='server2key', channels=[])
    demoServer3 = Server(
        name='demoServer3', description='A demo server for endpoint testing', serverImg='', serverInviteKey='server3key', channels=[])

    db.session.add(demoServer1)
    db.session.add(demoServer2)
    db.session.add(demoServer3)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_servers():
    db.session.execute('TRUNCATE servers RESTART IDENTITY CASCADE;')
    db.session.commit()
