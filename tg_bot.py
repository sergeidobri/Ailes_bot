from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

tg_bot_token='7025822278:AAGHEQ2bany8S72vrn-XVDDmC5FlJWXkUQY'

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    print(message)
    await message.reply("Слушаю, господин")


@dp.message_handler(commands=["ask"])
async def start_command(message: types.Message):
    await message.reply("Спроси вопрос")


@dp.message_handler(commands=["gosha"])
async def start_command(message: types.Message):
    await message.reply("Гоша, иди делай сайт давай")

executor.start_polling(dp)
