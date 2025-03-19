import asyncio
from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from API.api import sorted_low
from STATE.state import MyState
from database.add_database import add_user
from keyboards.number_keyboard_button import create_number_keyboard
from routers.handlers.default_handlers.text_commands import text


range_price_router = Router()


@range_price_router.message(Command("rangeprice"))
async def range_price(msg: Message, state: FSMContext):
    add_user(msg.from_user.id, msg.text.split()[0][1:])

    await state.set_state(MyState.price_check_in)
    await msg.answer(text='Введите цену от: ', reply_markup=ReplyKeyboardRemove())


@range_price_router.message(MyState.price_check_in, F.text)
async def city_states(msg: Message, state: FSMContext):
	await state.update_data(price_check_in=msg.text)

	await state.set_state(MyState.price_check_out)
	await msg.answer(text="Введите цену до: ", reply_markup=ReplyKeyboardRemove())


@range_price_router.message(MyState.price_check_out, F.text)
async def city_state(msg: Message, state: FSMContext):
    await state.update_data(price_check_out=msg.text)

    await state.set_state(MyState.count_in_button)
    await msg.answer(
        text='Выберете по сколько выводить товаров...',
        reply_markup=create_number_keyboard()
    )


@range_price_router.message(MyState.count_in_button)
async def count_button_user(msg: Message, state: FSMContext):
    await state.update_data(count_in_button=msg.text)

    try:
        await msg.answer(
            text="Нашел наушники по диапазону цены.", reply_markup=ReplyKeyboardRemove()
        )
        data = await state.get_data()

        count = 0
        for elem in sorted_low:
            if count >= int(data.get("count_in_button")):
                break

            if int(data.get("price_check_in")) < elem.get('salePriceU') < int(data.get("price_check_out")):
                await msg.answer(
                    text='Найдено {} предложений'.format(len(sorted_low))
                )
                await msg.answer(
                    text='Бренд: {}\nЦвет: {}\nЦена: {}\nЦена со скидкой: {}\nРейтинг: {}\nКоличесво отзывов: {}\nid: {}'.format(
                        elem.get('brand', None), elem.get('colors', None)[0]['name'], elem.get('priceU', None),
                        elem.get('salePriceU', None), elem.get('rating', None), elem.get('feedbacks', None),
                        elem.get('id', None))
                )
                await asyncio.sleep(1)
            count += 1

        await state.clear()
    except:
        await msg.answer(
            text='Не нашел наушники в этом диапазоне'
        )

    finally:
        await msg.answer(
            text=text
        )





