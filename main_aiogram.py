from aiogram import Bot, Dispatcher, executor, types
from keyboard_all import key_customer as kb_c

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply('Hi!', reply_markup=kb_c.greet_kb)
    # in this need create and check user hash-code from user-id
    log_it(f"{message.from_user.id} use /sart")

@dp.message_handler()
async def info(message: types.Message):
    """markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Site', callback_data='hello'))
    markup.add(types.InlineKeyboardButton('Hello', callback_data='hello'))
    await message.reply('Hello', reply_markup=markup)
    """
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(types.KeyboardButton('Site'))
    markup.add(types.KeyboardButton('WebSite'))
    markup.add(types.KeyboardButton('Styles'))
    await message.answer('Hello', reply_markup=markup)
    
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