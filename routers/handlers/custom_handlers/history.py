from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from database.get_database import get_data
from routers.handlers.default_handlers.text_commands import text

help_router = Router()


@help_router.message(Command("history"))
async def help_command(msg: Message):
    try:
        await msg.answer(
            text=get_data(msg.from_user.id)
        )
    except:
        await msg.answer(
            text='Cписок пуст!'
        )

    finally:
        await msg.answer(
            text=text
        )
