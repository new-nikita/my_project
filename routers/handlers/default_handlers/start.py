from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardRemove

from database.database import initialize_db, session, User

start_router = Router()


@start_router.message(CommandStart())
async def start_user_message(msg: Message):
    await msg.answer(
        text="Привет! Я бот для поиска наушников.\nИспользуй /help для получения списка команд.",
        reply_markup=ReplyKeyboardRemove()
    )
    initialize_db()
    user = User(id=msg.from_user.id, user_name=msg.from_user.username, date='')
    session.add(user)
    try:
        # подтверждаем транзакцию
        session.commit()
        print('Пользователь успешно добавлен!')
    except:
        # В случае ошибки откатываем транзакцию
        session.rollback()
        print('Произошла ошибка! Откатываем транзакцию.')
    finally:
        # закрываем сессию
        session.close()

