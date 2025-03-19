from loader import bot, dp
import asyncio
import logging


async def main():
    logging.basicConfig(level=logging.INFO)
    tbot = bot
    await dp.start_polling(tbot)


if __name__ == "__main__":
    asyncio.run(main())