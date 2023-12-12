from aiogram import Bot, Dispatcher
import telebot


token = ''
bot = telebot.TeleBot(token)
Bot = Bot(token)

dp = Dispatcher(Bot)
