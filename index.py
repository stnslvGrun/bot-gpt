import asyncio
import nest_asyncio
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.filters.command import Command
from aiogram import Bot, Dispatcher, types, F
from var import API_TOKEN, MESSAGE_BOT
from wiki import wiki_info

from g4f.client import Client

nest_asyncio.apply()
bot = Bot(token=API_TOKEN)
dp = Dispatcher()
client = Client()
list_title = []
list_theme = []

for wiki_dict in wiki_info:
    dict = {"role":"system","content":f"{wiki_dict.content}"}
    list_title.append(f"- {wiki_dict.title}")
    list_theme.append(dict)

async def keyboard(message):
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text="/help"))
    return builder

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    global MESSAGE_BOT
    MESSAGE_BOT = list_theme.copy()
    builder = await keyboard(message)
    await message.answer("GPT слушает. Может отвечать несколько секунд", reply_markup=builder.as_markup(resize_keyboard=True))

@dp.message(Command("termlist"))
async def termlist(message: types.Message):
    str_term = """Список локальных терминов:\n"""
    str_term += '\n'.join(list_title)
    await message.answer(str_term)
    
@dp.message(Command("help"))
async def help(message: types.Message):
    list_local_command = """
        Список команд\n/help \n/reset - сброс истории бота \n/termlist - список кастомных терминов'
    """
    await message.answer(list_local_command)

@dp.message(Command("reset"))
async def reset(message: types.Message):
    global MESSAGE_BOT
    MESSAGE_BOT = list_theme.copy()
    await message.answer("GPT слушает. История диалога сброшена")

@dp.message(F.text)
async def message_answer(message: types.Message):
    global MESSAGE_BOT
    msg_text = message.text
    MESSAGE_BOT.append({"role": "user", "content": f"{msg_text}"})
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=MESSAGE_BOT,
    )
    bot_msg = response.choices[0].message.content
    MESSAGE_BOT.append({"role": "assistant", "content": f"{bot_msg}"})
    await message.answer(bot_msg)

async def main():
    await dp.start_polling(bot)

asyncio.run(main())
