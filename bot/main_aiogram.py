import aiogram
from aiogram import Bot, Dispatcher, executor, types
from keyboard_all import key_customer as kb_c

from config import TOKEN
from config import LOG

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


"""
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply('', reply_markup=kb_c.greet_kb)
    # in this need create and check user hash-code from user-id
    log_it(f"{message.from_user.id} use /sart")
"""

@dp.message_handler(commands=['start'])
async def info(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton('Change Role'))
    markup.add(types.KeyboardButton('WebSite'))
    markup.add(types.KeyboardButton('Style'))
    await message.answer('Chose', reply_markup=markup)
    log_it(f"{message.from_user.id} use /sart")

@dp.message_handler(lambda message: message.text == 'Style')
async def handle_style(message: types.Message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item_preppy = types.InlineKeyboardButton('preppy', callback_data='preppy')
    item_casual = types.InlineKeyboardButton('casual', callback_data='casual')
    markup.add(item_preppy, item_casual)
    await message.reply("Выберите стиль:", reply_markup=markup)

@dp.callback_query_handler(lambda c: c.data in ['preppy', 'casual'])
async def handle_callback_query(callback_query: types.CallbackQuery):
    if callback_query.data == 'preppy':
        await bot.send_message(callback_query.from_user.id, "Вы выбрали стиль 'preppy'")
    elif callback_query.data == 'casual':
        await bot.send_message(callback_query.from_user.id, "Вы выбрали стиль 'casual'")


@dp.callback_query_handler()
async def callback(call):
    await call.message.answer(call.data)

def log_it(text):
    file_log = LOG
    with open (file_log, 'a') as file_l:
        file_l.write(f'{text}\n')

def create_inline_keyboard(file_path):
    keyboard = InlineKeyboardMarkup()

    with open(file_path, 'r') as file:
        for line in file:
            button_text = line.strip()
            button = InlineKeyboardButton(text=button_text, callback_data=button_text)
            keyboard.add(button)
    
    return keyboard

executor.start_polling(dp)