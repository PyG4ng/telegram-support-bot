from aiogram import F, Router
from aiogram.types import Message

echo_router = Router()


@echo_router.message(F.chat.type == "private")
async def echo_handler(message: Message) -> None:
    await message.copy_to(chat_id=message.from_user.id)  # type: ignore
