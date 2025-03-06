import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher

from config import settings
from support_bot.handlers.common import common_router
from support_bot.handlers.echo import echo_router

logger = logging.getLogger(__name__)


async def main() -> None:
    bot = Bot(settings.bot_token)
    dp = Dispatcher()
    dp.include_router(common_router)
    dp.include_router(echo_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Ctrl + C received, shutting down")
