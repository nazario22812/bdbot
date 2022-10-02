from distutils.cmd import Command
from aiogram import Bot, Dispatcher, executor, types
import logging
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://yto4ka:nazikking@cluster0.s2mmxuy.mongodb.net/?retryWrites=true&w=majority")
db = cluster["test-name"]
collection = db["test-collection"]


API_TOKEN = '5719756015:AAH8ij9KLsg1G5Fpb846RhOV49k0G3TTv7w'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    # await dp.bot.set_my_commands([types.BotCommand("/start", "restart the bot")])
    await message.answer("Hi!\nThis is database bot\nEnter /help for a list of commands")

@dp.message_handler(commands=['stop'])
async def send_welcome(message: types.Message):
    await message.answer("Bye-Bye✋")

async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("/start", "Restart the bot"),
        types.BotCommand("/stop", "Stop the bot"),
        types.BotCommand("/showbd", "Secret command for other users"),

    ])

@dp.message_handler(commands=["showbd"])
async def send_mobile(message: types.Message):
    await message.answer(f"Сlickable👇\nhttps://cloud.mongodb.com/v2/63389878b76abe577d2e9f3e#metrics/replicaSet/6338999b1468f14f26f39043/explorer/test-name/test-collection/find")

    

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=set_default_commands)