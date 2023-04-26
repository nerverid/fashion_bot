# author : Krivko Konstantin
# e-mail : nero.add@gmail.com
import telebot
from telebot import types

bot = telebot.Telebot('')

# Бот проверяет id пользователя.
# Выдаёт приветствие и текущий образ модели из последних загруженных
# Если пользователь не опознан предлагает \help
# \help - краткая справка и предлагает зарегистрироваться (для этого нужно выбрать пару опций)
# регистрация кнопки - покупатель;  продавец ; и кнопка выбора Мужчина - Женщина - А тебя волнует? (в этом случае будут обе категории, выпадать при каждом посещении)
# У покупателя и продавца разные меню
# Всегда есть кнопка сменить аккаунт - значит что поменять с покупателя на продавца и наоборот.
# У человека может быть одновременно два аккаунта.
# У покупателя кнопки "выбрать стиль" (появляется алфавитный рубрикатор по стилям)

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Styles")
        bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(message.form_user.id, "Question")

#Buttons - Styles
#Buttons - All looks
