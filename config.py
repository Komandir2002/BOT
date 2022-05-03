from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

TOKEN = config("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
URL = "https://bottima.herokuapp.com/"
URI = "postgres://bxasthyhjwhqvt:43f192e1962291f5ffdb142239c5c283837be1dca611fa23426234c194266b3e@ec2-3-211-6-217.compute-1.amazonaws.com:5432/d8n7hpjv3a79bm"
