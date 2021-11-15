from app.models import db, User, Server
def set_relationsips():
    added_server = Server.query.get(1)
    # print(added_server)
    user = User.query.get(1)
    user.serverList.append(added_server)

    db.session.commit()
