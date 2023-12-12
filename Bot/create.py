from aiogram import Bot, Dispatcher
import telebot


token = '6067792173:AAG1g-valcFkZ4XEbpQY8hhPLDXn5nPLoJQ'
bot = telebot.TeleBot(token)
Bot = Bot(token)

dp = Dispatcher(Bot)