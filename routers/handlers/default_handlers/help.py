from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove

from routers.handlers.default_handlers.text_commands import text


help_router = Router()

@help_router.message(Command("help"))
async def help_command(msg: Message):
	await msg.answer(
		text=text,
		reply_markup=ReplyKeyboardRemove()

	)