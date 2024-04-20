import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from Parsing import total_pars

tg_bot_token = '7025822278:AAGHEQ2bany8S72vrn-XVDDmC5FlJWXkUQY'

bot = Bot(token=tg_bot_token)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Контакты РУДН"),
            types.KeyboardButton(text="Гоша"),
            types.KeyboardButton(text="Вопрос"),
            types.KeyboardButton(text="Ссылочки"),
            types.KeyboardButton(text="Созыв"),
            types.KeyboardButton(text="Команды")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Запрос"
    )
    await message.answer("Что-бы посмотреть комманды введите /commands", reply_markup=keyboard)

from aiogram import F


@dp.message(F.text == "Контакты РУДН")
async def without_puree(message: types.Message):
    await message.reply('Номера различных сотрудников:\n\n' + total_pars())


@dp.message(Command('gosha'))
@dp.message(F.text == "Гоша")
async def with_puree(message: types.Message):
    await message.reply("@Grey_Uncle, иди делай сайт давай")

@dp.message(Command('all'))
@dp.message(F.text == "Созыв")
async def with_puree(message: types.Message):
    await message.reply("Я вызываю вас: (@Grey_Uncle, @No_name24555, @returnanything, @shvarzneger, @bom_non)")


@dp.message(F.text == "Вопрос")
@dp.message(Command('ask'))
async def start_command(message: Message):
    await message.answer("Спроси вопрос")




@dp.message(F.text == "Команды")
@dp.message(Command('commands'))
async def start_command(message: Message):
    await message.answer("/all\n/ask\n/gosha\n/commands\n/inline_url")

@dp.message(F.text == 'Ссылочки')
@dp.message(Command('inline_url'))
async def cmd_inline_url(message: types.Message, bot: Bot):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Наш GitHub", url="https://github.com/Orlov-Oleg-Igorevich/AilesNew")
    )
    builder.row(types.InlineKeyboardButton(
        text='Социальная сеть "Ailes"',
        url="https://ya.ru/")
    )

    await message.answer(
        'Выберите ссылку',
        reply_markup=builder.as_markup(),
    )



async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())