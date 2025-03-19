import asyncio
from aiogram import Router
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from STATE.state import MyState
from API.api import sorted_low
from database.add_database import add_user
from keyboards.number_keyboard_button import create_number_keyboard
from routers.handlers.default_handlers.text_commands import text


lowprise_router = Router()


@lowprise_router.message(Command("low"))
async def low(msg: Message, state: FSMContext):
    add_user(msg.from_user.id, msg.text.split()[0][1:])

    await state.set_state(MyState.count_in_button)
    await msg.answer(
        text='Выберете по сколько выводить товаров...',
        reply_markup=create_number_keyboard()
    )


@lowprise_router.message(MyState.count_in_button)
async def count_button_user(msg: Message, state: FSMContext):
    await state.update_data(count_in_button=msg.text)

    data = await state.get_data()
    get_date = data.get("count_in_button")

    await msg.answer(text="Нашел наушники по возрастанию цены.", reply_markup=ReplyKeyboardRemove())

    count = 0
    for elem in sorted_low:
        if count >= int(get_date):
            break

        await msg.answer(
        	text='Бренд: {}\nЦвет: {}\nЦена: {}\nЦена со скидкой: {}\nРейтинг: {}\nКоличесво отзывов: {}\nid: {}'.format(
            	elem.get('brand', None), elem.get('colors', None), elem.get('priceU', None), elem.get('salePriceU', None), elem.get('rating', None), elem.get('feedbacks', None), elem.get('id', None))
        )
        await asyncio.sleep(1)
        count += 1

    await state.clear()

    await msg.answer(
        text=text
    )


