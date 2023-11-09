from config import TOKEN

from aiogram.utils import executor
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage import MemoryStorage

async def __on_start_up(dp: Dispatcher) -> None:
    pass

def start_bot():
    bot = Bot(token=TOKEN)
    dp = Dispatcher(bot, storage=MemoryStorage())
    executor.start_polling(dp, skip_updates=True, on_startup=__on_start_up)