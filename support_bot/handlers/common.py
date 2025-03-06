from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from config import settings

common_router = Router(name="common")


@common_router.message(F.chat.type == "private", CommandStart())
async def handle_start(message: Message):
    await message.answer(text=settings.welcome_message)


@common_router.message(F.chat.type == "private", Command("help"))
async def handle_help(message: Message):
    await message.answer(text=settings.help_message)
