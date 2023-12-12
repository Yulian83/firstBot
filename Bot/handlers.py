from create import dp, bot
from aiogram import types
from telebot import types
from Algorithm_Basics import *
from Top12Algorithms import *
from logger import *


category =  ''
order = []


@dp.message_handler(commands=["start","help"])
def welcome(message):

    registration = types.InlineKeyboardMarkup()
    registration.row_wigth = 1
    registration.add(types.InlineKeyboardButton(text='\U00002728 Главное меню', callback_data='main_menu'))
    bot.send_message(message.chat.id, text='Привет! Я бот Forder, помогу тебе разобраться в алгоритмах🥳', reply_markup=registration)



@dp.callback_query_handler(lambda call: True) #проверка на получение callback-ов
def query_handler_base(call):

    if call.data == 'main_menu':
        main_menu = types.InlineKeyboardMarkup()
        main_menu.row_width = 1
        main_menu.add(types.InlineKeyboardButton(text = '😎 Основы алгоритмов', callback_data='Algorithm_Basics'))
        main_menu.add(types.InlineKeyboardButton(text = '🙌 9 алгоритмов, которые должен знать каждый разработчик: объясняем на гифках', callback_data='Top12Algorithms'))

        bot.send_message(call.message.chat.id, text='\U0001F4DC Главное меню', reply_markup=main_menu)
        
        bot.edit_message_text(call.message.chat.id, call.message.message_id, text=None)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup= None) #убираем кнопки
        bot.answer_callback_query(call.id, text='') #ответ на callback

    AlgorithmBasics(call)
    Top12Algorithms(call)
