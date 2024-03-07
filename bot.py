import asyncio
import logging
from aiogram import Bot, Dispatcher

from core.config import config
from handlers import questions


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    bot = Bot(token=config.bot_token)
    dp = Dispatcher()

    dp.include_router(
        questions.router
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
