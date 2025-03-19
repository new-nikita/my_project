from database.database import User, session


def add_user(user_id, command):
    user_to_update = session.query(User).filter_by(id=user_id).first()
    user_to_update.date = '/{}  {}'.format(command, user_to_update.date)

    session.commit()  # Сохранение изменений
    print('Команда записана')
