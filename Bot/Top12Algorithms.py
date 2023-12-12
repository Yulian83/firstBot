from logger import *
from handlers import *

def FinalSendMessage(call, message, menu):
    bot.send_message(call.message.chat.id, text=message, reply_markup=menu)
    bot.edit_message_reply_markup(call.message.chat.id, reply_markup = None)
    bot.answer_callback_query(call.id, text='')



def CreateMenuList(page: str):

    menu_list = types.InlineKeyboardMarkup()
    menu_list.add(types.InlineKeyboardButton(text='\u27A1\uFE0F Далее', callback_data=page)) 
    menu_list.add(types.InlineKeyboardButton(text='\U0001F4DC К оглавлению', callback_data='Top12Algorithms')) 
    
    return menu_list






def Top12Algorithms(call):
    global Top12AlgorithmsText
    if call.data == 'Top12Algorithms':
        
        menu = types.InlineKeyboardMarkup()
        menu.add(types.InlineKeyboardButton(text='Бинарный поиск', callback_data='2_page_1_1')) 
        menu.add(types.InlineKeyboardButton(text='Сортировки пузырьком, выбором, вставками', callback_data='2_page_2_1')) 
        menu.add(types.InlineKeyboardButton(text='Быстрая сортировка и сортировка слиянием', callback_data='2_page_3_1')) 
        menu.add(types.InlineKeyboardButton(text='Кодирование Хаффмена', callback_data='page_4_1')) 
        menu.add(types.InlineKeyboardButton(text='Поиск в ширину', callback_data='2_page_5_1')) 
        menu.add(types.InlineKeyboardButton(text='Поиск в глубину', callback_data='2_page_6_1')) 
        menu.add(types.InlineKeyboardButton(text='Градиентный спуск', callback_data='2_page_7_1')) 
        menu.add(types.InlineKeyboardButton(text='Алгоритм Дейкстры', callback_data='2_page_8_1')) 
        menu.add(types.InlineKeyboardButton(text='Обмен ключами Диффи-Хеллмана', callback_data='2_page_9_1')) 
        menu.add(types.InlineKeyboardButton(text='\U0001F519 Назад в главное меню', callback_data='main_menu'))

        FinalSendMessage(call, '\U0001F4DC Оглавление', menu)

    elif call.data == '2_page_1_1':   
        
        Top12AlgorithmsText = Read_DB("Top12Algorithms", "data2")

        FinalSendMessage(call, Top12AlgorithmsText[0], CreateMenuList("2_page_1_2"))


    elif call.data == '2_page_1_2':   
        
        bot.send_animation(call.message.chat.id, open("2 course 1 semestr\\bot\data2\img\\1.gif", 'rb'))

        FinalSendMessage(call, Top12AlgorithmsText[1], CreateMenuList("2_page_2_1"))

    elif call.data == '2_page_2_1':   
        
        Top12AlgorithmsText = Read_DB("Top12Algorithms2", "data2")

        bot.send_animation(call.message.chat.id, open("2 course 1 semestr\\bot\data2\img\\2.gif", 'rb'))
        bot.send_message(call.message.chat.id, text="Сортировка пузырьком")

        bot.send_animation(call.message.chat.id, open("2 course 1 semestr\\bot\data2\img\\3.gif", 'rb'))
        bot.send_message(call.message.chat.id, text="Сортировка выбором")

        bot.send_animation(call.message.chat.id, open("2 course 1 semestr\\bot\data2\img\\4.gif", 'rb'))
        bot.send_message(call.message.chat.id, text="Сортировка вставками")

        FinalSendMessage(call, Top12AlgorithmsText[0], CreateMenuList("2_page_3_1"))


    elif call.data == '2_page_3_1':   
        
        Top12AlgorithmsText = Read_DB("Top12Algorithms3", "data2")

        bot.send_animation(call.message.chat.id, open("2 course 1 semestr\\bot\data2\img\\5.gif", 'rb'))
        bot.send_message(call.message.chat.id, text="Быстрая сортировка")
        bot.send_animation(call.message.chat.id, open("2 course 1 semestr\\bot\data2\img\\6.gif", 'rb'))
        bot.send_message(call.message.chat.id, text="Сортировка слиянием")

        FinalSendMessage(call, Top12AlgorithmsText[0], CreateMenuList("2_page_4_1"))


    elif call.data == '2_page_4_1':   
        
        Top12AlgorithmsText = Read_DB("Top12Algorithms4", "data2")

        FinalSendMessage(call, Top12AlgorithmsText[0], CreateMenuList("2_page_4_2"))


    elif call.data == '2_page_4_2':   
        
        bot.send_animation(call.message.chat.id, open("2 course 1 semestr\\bot\data2\img\\7.gif", 'rb'))

        FinalSendMessage(call, Top12AlgorithmsText[1], CreateMenuList("2_page_5_1"))


    elif call.data == '2_page_5_1':   
        Top12AlgorithmsText = Read_DB("Top12Algorithms5", "data2")

        FinalSendMessage(call, Top12AlgorithmsText[0], CreateMenuList("2_page_5_2"))

    elif call.data == '2_page_5_2':   

        bot.send_animation(call.message.chat.id, open("2 course 1 semestr\\bot\data2\img\\8.gif", 'rb'))

        FinalSendMessage(call, Top12AlgorithmsText[1], CreateMenuList("2_page_6_1"))

    elif call.data == '2_page_6_1':   
        Top12AlgorithmsText = Read_DB("Top12Algorithms6", "data2")

        FinalSendMessage(call, Top12AlgorithmsText[0], CreateMenuList("2_page_6_2"))

        
    elif call.data == '2_page_6_2':   

        bot.send_animation(call.message.chat.id, open("2 course 1 semestr\\bot\data2\img\\9.gif", 'rb'))

        FinalSendMessage(call, Top12AlgorithmsText[1], CreateMenuList("2_page_7_1"))


    elif call.data == '2_page_7_1':   
    
        Top12AlgorithmsText = Read_DB("Top12Algorithms7", "data2")

        FinalSendMessage(call, Top12AlgorithmsText[0], CreateMenuList("2_page_7_2"))


    elif call.data == '2_page_7_2':   

        bot.send_animation(call.message.chat.id, open("2 course 1 semestr\\bot\data2\img\\10.gif", 'rb'))

        FinalSendMessage(call, Top12AlgorithmsText[1], CreateMenuList("2_page_8_1"))

    elif call.data == '2_page_8_1':   

        Top12AlgorithmsText = Read_DB("Top12Algorithms8", "data2")

        FinalSendMessage(call, Top12AlgorithmsText[0], CreateMenuList("2_page_8_2"))

    elif call.data == '2_page_8_2':   


        bot.send_animation(call.message.chat.id, open("2 course 1 semestr\\bot\data2\img\\11.gif", 'rb'))

        FinalSendMessage(call, Top12AlgorithmsText[1], CreateMenuList("2_page_9_1"))

    elif call.data == '2_page_9_1':   

        Top12AlgorithmsText = Read_DB("Top12Algorithms9", "data2")

        FinalSendMessage(call, Top12AlgorithmsText[0], CreateMenuList("2_page_9_2"))

    elif call.data == '2_page_9_2':   


        bot.send_animation(call.message.chat.id, open("2 course 1 semestr\\bot\data2\img\\12.gif", 'rb'))
        menu_list = types.InlineKeyboardMarkup()
        menu_list.add(types.InlineKeyboardButton(text='К оглавлению', callback_data='Top12Algorithms')) 

        FinalSendMessage(call, Top12AlgorithmsText[1], menu_list)


  