from aiogram import Bot, Dispatcher
from config_date import config
from routers import router as main_router


bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher()

dp.include_router(main_router)