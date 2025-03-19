from database.database import session, User


def get_data(user_id):
    user_to_get = session.query(User).filter_by(id=user_id).first()
    get_command = user_to_get.date
    return get_command



