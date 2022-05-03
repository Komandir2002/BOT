from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

TOKEN = config("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
URL = "https://bottima.herokuapp.com/"
URI = "postgres://wdkyuubratcmul:e2c92f9a6d497a841182f53b75df14f74272cbe4f2ed9b013b4b1b0da3045ea8@ec2-3-224-164-189.compute-1.amazonaws.com:5432/d6r439rigcc8lo"
