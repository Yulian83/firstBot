from handlers import *
from logger import *

def FinalSendMessage(call, message: str, menu):
    bot.send_message(call.message.chat.id, text=message, reply_markup=menu)
    bot.edit_message_reply_markup(call.message.chat.id, reply_markup = None)
    bot.answer_callback_query(call.id, text='')

def CreateMenuList(page: str):

    menu_list = types.InlineKeyboardMarkup()
    menu_list.add(types.InlineKeyboardButton(text='\u27A1\uFE0F Далее', callback_data=page)) 
    menu_list.add(types.InlineKeyboardButton(text='\U0001F4DC К оглавлению', callback_data='Algorithm_Basics')) 

    return menu_list



def AlgorithmBasics(call):
    global AlgorithmBasicsText
    if call.data == 'Algorithm_Basics':
        
        menu = types.InlineKeyboardMarkup()
        menu.add(types.InlineKeyboardButton(text='Что такое алгоритмы', callback_data='page_1_1')) 
        menu.add(types.InlineKeyboardButton(text='Для чего их используют', callback_data='page_2_1')) 
        menu.add(types.InlineKeyboardButton(text='Какие у них есть свойства', callback_data='page_3_1')) 
        menu.add(types.InlineKeyboardButton(text='Что такое псевдокод', callback_data='page_4_1')) 
        menu.add(types.InlineKeyboardButton(text='Что такое блок-схемы и как их рисовать', callback_data='page_5_1')) 
        menu.add(types.InlineKeyboardButton(text='Примеры линейных, ветвящихся, циклических и рекурсивных алгоритмов и блок-схем', callback_data='page_6_1')) 
        menu.add(types.InlineKeyboardButton(text='\U0001F519 Назад в главное меню', callback_data='main_menu'))

        FinalSendMessage(call, "\U0001F4DC Оглавление", menu)

    elif call.data == 'page_1_1':   
        
        AlgorithmBasicsText = Read_DB("AlgorithmBasicsText", "data")

        FinalSendMessage(call, AlgorithmBasicsText[0], CreateMenuList('page_1_2'))

    elif call.data == 'page_1_2':   

        FinalSendMessage(call, AlgorithmBasicsText[1], CreateMenuList('page_1_22'))


    elif call.data == 'page_1_22':   

        FinalSendMessage(call, AlgorithmBasicsText[2], CreateMenuList('page_1_3'))

        
    elif call.data == 'page_1_3':   
    
        FinalSendMessage(call, f'''
{AlgorithmBasicsText[3]}
{AlgorithmBasicsText[4]}
{AlgorithmBasicsText[5]}
{AlgorithmBasicsText[6]}
{AlgorithmBasicsText[7]}
{AlgorithmBasicsText[8]}
{AlgorithmBasicsText[9]}''', CreateMenuList('page_1_4'))


    elif call.data == 'page_1_4':   

        FinalSendMessage(call, AlgorithmBasicsText[10], CreateMenuList('page_1_5'))

    elif call.data == 'page_1_5':   

        FinalSendMessage(call, AlgorithmBasicsText[11], CreateMenuList('page_1_6'))

    elif call.data == 'page_1_6':   

        FinalSendMessage(call, f'''
{AlgorithmBasicsText[12]}
{AlgorithmBasicsText[13]}
{AlgorithmBasicsText[14]}
{AlgorithmBasicsText[15]}
{AlgorithmBasicsText[16]}
{AlgorithmBasicsText[17]}
{AlgorithmBasicsText[18]}
{AlgorithmBasicsText[19]}
{AlgorithmBasicsText[20]}
{AlgorithmBasicsText[21]}
{AlgorithmBasicsText[22]}
{AlgorithmBasicsText[23]}
{AlgorithmBasicsText[24]}
{AlgorithmBasicsText[25]}
{AlgorithmBasicsText[26]}
{AlgorithmBasicsText[27]}
{AlgorithmBasicsText[28]}''', CreateMenuList('page_1_7'))

    elif call.data == 'page_1_7':   

        FinalSendMessage(call, AlgorithmBasicsText[29], CreateMenuList('page_1_8'))


    elif call.data == 'page_1_8':   

        FinalSendMessage(call, AlgorithmBasicsText[30], CreateMenuList('page_1_9'))


    elif call.data == 'page_1_9':   

        FinalSendMessage(call, AlgorithmBasicsText[31], CreateMenuList('page_2_1'))


    elif call.data == 'page_2_1':   
        
        AlgorithmBasicsText = Read_DB("AlgorithmBasicsText2", "data")

        FinalSendMessage(call, AlgorithmBasicsText[0], CreateMenuList('page_2_2'))


    elif call.data == 'page_2_2':   

        FinalSendMessage(call, AlgorithmBasicsText[1], CreateMenuList('page_2_3'))


    elif call.data == 'page_2_3':   

        FinalSendMessage(call, AlgorithmBasicsText[2], CreateMenuList('page_2_4'))


    elif call.data == 'page_2_4':   

        FinalSendMessage(call, AlgorithmBasicsText[3], CreateMenuList('page_2_5'))


    elif call.data == 'page_2_5':   
        
        FinalSendMessage(call, AlgorithmBasicsText[4], CreateMenuList('page_2_6'))

    elif call.data == 'page_2_6':   

        FinalSendMessage(call, AlgorithmBasicsText[5], CreateMenuList('page_2_7'))

    elif call.data == 'page_2_7':   

        FinalSendMessage(call, AlgorithmBasicsText[6], CreateMenuList('page_2_8'))

    elif call.data == 'page_2_8':   

        FinalSendMessage(call, AlgorithmBasicsText[7], CreateMenuList('page_2_9'))

    elif call.data == 'page_2_9':   

        FinalSendMessage(call, AlgorithmBasicsText[8], CreateMenuList('page_2_10'))

    elif call.data == 'page_2_10':   

        FinalSendMessage(call, AlgorithmBasicsText[9], CreateMenuList('page_2_11'))

    elif call.data == 'page_2_11':   

        FinalSendMessage(call, AlgorithmBasicsText[10], CreateMenuList('page_2_12'))

    elif call.data == 'page_2_12':   

        FinalSendMessage(call, AlgorithmBasicsText[11], CreateMenuList('page_3_1'))


    elif call.data == 'page_3_1':   

        AlgorithmBasicsText = Read_DB("AlgorithmBasicsText3", "data")

        FinalSendMessage(call, AlgorithmBasicsText[0], CreateMenuList('page_3_2'))

    elif call.data == 'page_3_2':   

        FinalSendMessage(call, f'''
{AlgorithmBasicsText[1]}
{AlgorithmBasicsText[2]}
{AlgorithmBasicsText[3]}
{AlgorithmBasicsText[4]}
{AlgorithmBasicsText[5]}
{AlgorithmBasicsText[6]}''', CreateMenuList('page_3_3'))

    elif call.data == 'page_3_3':   

        FinalSendMessage(call, AlgorithmBasicsText[7], CreateMenuList('page_3_4'))

    elif call.data == 'page_3_4':   

        FinalSendMessage(call, AlgorithmBasicsText[8], CreateMenuList('page_3_5'))

    elif call.data == 'page_3_5':   

        FinalSendMessage(call, AlgorithmBasicsText[9], CreateMenuList('page_3_6'))


    elif call.data == 'page_3_6':   

        FinalSendMessage(call, AlgorithmBasicsText[10], CreateMenuList('page_3_7'))


    elif call.data == 'page_3_7':   

        FinalSendMessage(call, AlgorithmBasicsText[11], CreateMenuList('page_3_8'))


    elif call.data == 'page_3_8':   

        FinalSendMessage(call, AlgorithmBasicsText[12], CreateMenuList('page_3_9'))


    elif call.data == 'page_3_9':   

        FinalSendMessage(call, AlgorithmBasicsText[13], CreateMenuList('page_4_1'))


    elif call.data == 'page_4_1':   

        AlgorithmBasicsText = Read_DB("AlgorithmBasicsText4", "data")

        FinalSendMessage(call, AlgorithmBasicsText[0], CreateMenuList('page_4_2'))

    elif call.data == 'page_4_2':   

        FinalSendMessage(call, AlgorithmBasicsText[1], CreateMenuList('page_4_3'))

    elif call.data == 'page_4_3':   

        FinalSendMessage(call, AlgorithmBasicsText[2], CreateMenuList('page_4_4'))

    elif call.data == 'page_4_4':   
        
        bot.send_photo(call.message.chat.id, open("2 course 1 semestr\\bot\data\img\\1.bmp", 'rb'))

        FinalSendMessage(call, AlgorithmBasicsText[3], CreateMenuList('page_4_5'))

    elif call.data == 'page_4_5':   
        
        bot.send_photo(call.message.chat.id, open("2 course 1 semestr\\bot\data\img\\2.bmp", 'rb'))

        FinalSendMessage(call, AlgorithmBasicsText[4], CreateMenuList('page_4_6'))

    elif call.data == 'page_4_6':   

        FinalSendMessage(call, AlgorithmBasicsText[5], CreateMenuList('page_5_1'))


    elif call.data == 'page_5_1':   
        AlgorithmBasicsText = Read_DB("AlgorithmBasicsText5", "data")

        FinalSendMessage(call, AlgorithmBasicsText[0], CreateMenuList('page_5_2'))

    elif call.data == 'page_5_2':   

        FinalSendMessage(call, AlgorithmBasicsText[1], CreateMenuList('page_5_3'))

    elif call.data == 'page_5_3':   

        bot.send_photo(call.message.chat.id, open("2 course 1 semestr\\bot\data\img\\3.bmp", 'rb'))
        bot.send_photo(call.message.chat.id, open("2 course 1 semestr\\bot\data\img\\4.bmp", 'rb'))
        bot.send_photo(call.message.chat.id, open("2 course 1 semestr\\bot\data\img\\5.bmp", 'rb'))

        FinalSendMessage(call, AlgorithmBasicsText[2], CreateMenuList('page_5_4'))

    elif call.data == 'page_5_4':   

        FinalSendMessage(call, AlgorithmBasicsText[3], CreateMenuList('page_5_5'))

    elif call.data == 'page_5_5':   

        FinalSendMessage(call, AlgorithmBasicsText[4], CreateMenuList('page_5_6'))

    elif call.data == 'page_5_6':   

        FinalSendMessage(call, AlgorithmBasicsText[5], CreateMenuList('page_6_1'))
        

    elif call.data == 'page_6_1':   

        AlgorithmBasicsText = Read_DB("AlgorithmBasicsText6", "data")

        FinalSendMessage(call, AlgorithmBasicsText[0], CreateMenuList('page_6_2'))

    elif call.data == 'page_6_2':   

        FinalSendMessage(call, AlgorithmBasicsText[1], CreateMenuList('page_6_3'))

    elif call.data == 'page_6_3':   

        FinalSendMessage(call, AlgorithmBasicsText[2], CreateMenuList('page_6_4'))

    elif call.data == 'page_6_4':   

        FinalSendMessage(call, AlgorithmBasicsText[3], CreateMenuList('page_6_5'))

    elif call.data == 'page_6_5':   
        
        bot.send_photo(call.message.chat.id, open("2 course 1 semestr\\bot\data\img\\6.bmp", 'rb'))

        FinalSendMessage(call, AlgorithmBasicsText[4], CreateMenuList('page_6_6'))

    elif call.data == 'page_6_6':   
        
        bot.send_photo(call.message.chat.id, open("2 course 1 semestr\\bot\data\img\\7.bmp", 'rb'))

        FinalSendMessage(call, AlgorithmBasicsText[5], CreateMenuList('page_6_7'))

    elif call.data == 'page_6_7':   

        FinalSendMessage(call, AlgorithmBasicsText[6], CreateMenuList('page_6_8'))

    elif call.data == 'page_6_8':   

        FinalSendMessage(call, AlgorithmBasicsText[7], CreateMenuList('page_6_9'))

    elif call.data == 'page_6_9':   
 
        FinalSendMessage(call, AlgorithmBasicsText[8], CreateMenuList('page_6_10'))

    elif call.data == 'page_6_10':   
        
        bot.send_photo(call.message.chat.id, open("2 course 1 semestr\\bot\data\img\\8.png", 'rb'))

        FinalSendMessage(call, AlgorithmBasicsText[9], CreateMenuList('page_6_11'))

    elif call.data == 'page_6_11':   
        
        bot.send_photo(call.message.chat.id, open("2 course 1 semestr\\bot\data\img\\9.bmp", 'rb'))

        FinalSendMessage(call, AlgorithmBasicsText[10], CreateMenuList('page_6_12'))

    elif call.data == 'page_6_12':   

        FinalSendMessage(call, AlgorithmBasicsText[11], CreateMenuList('page_6_13'))

    elif call.data == 'page_6_13':   

        FinalSendMessage(call, AlgorithmBasicsText[12], CreateMenuList('page_6_14'))

    elif call.data == 'page_6_14':   

        FinalSendMessage(call, AlgorithmBasicsText[13], CreateMenuList('page_6_15'))

    elif call.data == 'page_6_15':   

        FinalSendMessage(call, AlgorithmBasicsText[14], CreateMenuList('page_6_16'))

    elif call.data == 'page_6_16':   
        
        bot.send_photo(call.message.chat.id, open("2 course 1 semestr\\bot\data\img\\10.png", 'rb'))

        FinalSendMessage(call, AlgorithmBasicsText[15], CreateMenuList('page_6_17'))

    elif call.data == 'page_6_17':   
        
        bot.send_photo(call.message.chat.id, open("2 course 1 semestr\\bot\data\img\\11.bmp", 'rb'))

        FinalSendMessage(call, AlgorithmBasicsText[16], CreateMenuList('page_6_18'))

    elif call.data == 'page_6_18':   
        
        bot.send_photo(call.message.chat.id, open("2 course 1 semestr\\bot\data\img\\12.bmp", 'rb'))

        FinalSendMessage(call, AlgorithmBasicsText[17], CreateMenuList('page_6_19'))

    elif call.data == 'page_6_19':   

        FinalSendMessage(call, AlgorithmBasicsText[18], CreateMenuList('page_6_20'))

    elif call.data == 'page_6_20':   

        FinalSendMessage(call, AlgorithmBasicsText[19], CreateMenuList('page_6_21'))

    elif call.data == 'page_6_21':   
        
        bot.send_photo(call.message.chat.id, open("2 course 1 semestr\\bot\data\img\\13.bmp", 'rb'))

        FinalSendMessage(call, AlgorithmBasicsText[20], CreateMenuList('page_6_22'))

    elif call.data == 'page_6_22':   
        
        bot.send_photo(call.message.chat.id, open("2 course 1 semestr\\bot\data\img\\14.png", 'rb'))

        FinalSendMessage(call, AlgorithmBasicsText[21], CreateMenuList('page_6_23'))

    elif call.data == 'page_6_23':   
        
        FinalSendMessage(call, AlgorithmBasicsText[22], CreateMenuList('page_6_24'))

    elif call.data == 'page_6_24':   
        

        menu_list = types.InlineKeyboardMarkup()
        menu_list.add(types.InlineKeyboardButton(text='К оглавлению', callback_data='Algorithm_Basics')) 

        FinalSendMessage(call, AlgorithmBasicsText[23], menu_list)
