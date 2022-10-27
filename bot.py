from email import message 
from email.mime import image
import logging
from tkinter import PhotoImage, image_names, image_types
from telegram import Chat, Update
from telegram.ext import CallbackContext, CommandHandler, Updater, MessageHandler, Filters
import requests 
import webbrowser
from PIL import Image



# States
START = 1
Fruit_1 = 2
Fruit_2 = 3
Fruit_3 = 4
Fruit_4 = 5
Fruit_5 = 6
Fruit_6 = 7
Fruit_7 = 8
Fruit_8 = 9
Fruit_9 = 10
Fruit_10 = 11
Fruit_11 = 12
Fruit_12 = 13


user_states = {}

updater = Updater(token="5723412226:AAHk0mHt4epfpc-gx2x1HEeigz7h_NZ7o0o", use_context=True)
dispatcher = updater.dispatcher

def start_command_handler(update: Update, context: CallbackContext):
    global user_states
    
    user_id = update.effective_chat.id
    
    # If user not in states - add him / her
    if user_id not in user_states:
        user_states[user_id] = START
        
    print(f"[/start]: current user state: {user_states[user_id]}")
    
    # Check state of current user
    if user_states[user_id] == START:
        text = "Перевіримо як ти знєш фрукти \n1: Так\n2: Ні"
        url1='https://agropolit.com/media/news/o-o-w/00/17/17529/ya-23991.jpg'
        img1=url1
        context.bot.send_message(chat_id=update.effective_chat.id, text=text)
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=img1)
        user_states[user_id] +=1
    else:
        pass

def text_message_handler(update: Update, context: CallbackContext):
    message = update.message.text
    user_id = update.effective_chat.id
    
    
    global user_states
    
    print(f"[text]: current user state: {user_states[user_id]}")
    
    if user_states[user_id] == Fruit_1:
        if message == "1":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Хороший вибір\nЩо це за Фрукт" )
            text = "\n1 Банан \n2 Апельсин \n3 Яблуко \n4 Абрикос \n5 Мандарин \n6 Папая \n7 Вишня \n11 Виноград \n8 Сливка \n9 Груша \n10 Маракуя"
            img2="https://cdnn21.img.ria.ru/images/49873/01/498730163_0:177:2928:1824_1920x0_80_0_0_93fb227fb06f559b14009d1939cdf718.jpg"
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=img2)
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
            user_states[user_id] += 1
        elif message == "2":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Поганий вибір")
            user_states[user_id] = 1
            text = "Гра закінчилась. Введіть /start, щоб почати знову."
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
    elif user_states[user_id] == Fruit_2:
        if message == "1":
            img3="https://img2.zakaz.ua/02.1601640953.ad72436478c_2020-10-02_Julia/02.1601640953.SNCPSG10.obj.0.1.jpg.oe.jpg.pf.jpg.1350nowm.jpg.1350x.jpg"
            context.bot.send_message(chat_id=update.effective_chat.id, text="Правельно")
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=img3)
            text = "\n1 Банан \n2 Апельсин \n3 Яблуко \n4 Абрикос \n5 Мандарин \n6 Папая \n7 Вишня \n11 Виноград \n8 Сливка \n9 Груша \n10 Маракуя"
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
            user_states[user_id] += 1
        elif message == "2":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "3":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "4":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "5":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "6":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "7":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "8":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "9":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "10":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
    elif user_states[user_id] == Fruit_3:
        if message == "3":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Правельно")
            img4="https://896479.smushcdn.com/2111889/wp-content/uploads/2021/11/image-6-1024x682.jpeg?size=1024x682&lossy=1&strip=1&webp=1"
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=img4)
            text = "\n1 Банан \n2 Апельсин \n3 Яблуко \n4 Абрикос \n5 Мандарин \n6 Папая \n7 Вишня \n11 Виноград \n8 Сливка \n9 Груша \n10 Маракуя"
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
            user_states[user_id] += 1
        elif message == "2":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "1":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "4":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "5":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "6":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "7":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "8":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "9":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "10":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
    elif user_states[user_id] == Fruit_4:
        if message == "2":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Правельно")
            img5="https://domicad.com.ua/uploads/catalog_products/abrikos-shedevr_1.jpg"
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=img5)
            text = "\n1 Банан \n2 Апельсин \n3 Яблуко \n4 Абрикос \n5 Мандарин \n6 Папая \n7 Вишня \n11 Виноград \n8 Сливка \n9 Груша \n10 Маракуя"
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
            user_states[user_id] += 1
        elif message == "4":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "1":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "3":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "5":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "6":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "7":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "8":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "9":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "10":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
    elif user_states[user_id] == Fruit_5:
        if message == "4":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Правельно")
            img6="https://domicad.com.ua/uploads/catalog_products/grusha-medovaya_1.jpg"
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=img6)
            text = "\n1 Банан \n2 Апельсин \n3 Яблуко \n4 Абрикос \n5 Мандарин \n6 Папая \n7 Вишня \n11 Виноград \n8 Сливка \n9 Груша \n10 Маракуя"
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
            user_states[user_id] += 1
        elif message == "2":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "1":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "3":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "5":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "6":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "7":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "8":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "9":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "10":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
    elif user_states[user_id] == Fruit_6:
        if message == "9":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Правельно")
            img7="https://poli-klinika.com.ua/files/news/rm_rus/1-1-700x506.jpg"
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=img7)
            text = "\n1 Банан \n2 Апельсин \n3 Яблуко \n4 Абрикос \n5 Мандарин \n6 Папая \n7 Вишня \n11 Виноград \n8 Сливка \n9 Груша \n10 Маракуя"
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
            user_states[user_id] += 1
        elif message == "2":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "1":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "3":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "5":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "6":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "7":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "8":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "9":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "10":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "11":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "4":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
    elif user_states[user_id] == Fruit_7:
        if message == "7":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Правельно")
            img8="https://m.dom-eda.com/uploads/images/catalog/item/53275a4f46/c4f7252f9e_1000.jpg"
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=img8)
            text = "\n1 Банан \n2 Апельсин \n3 Яблуко \n4 Абрикос \n5 Мандарин \n6 Папая \n7 Вишня \n11 Виноград \n8 Сливка \n9 Груша \n10 Маракуя"
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
            user_states[user_id] += 1
        elif message == "2":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "1":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "3":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "5":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "6":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "7":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "8":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "9":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "10":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "11":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "4":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
    elif user_states[user_id] == Fruit_8:
        if message == "5":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Правельно")
            img9="https://vinograd.info/images/sorta/r/roshfor/roshfor-3.jpg"
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=img9)
            text = "\n1 Банан \n2 Апельсин \n3 Яблуко \n4 Абрикос \n5 Мандарин \n6 Папая \n7 Вишня \n11 Виноград \n8 Сливка \n9 Груша \n10 Маракуя"
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
            user_states[user_id] += 1
        elif message == "2":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "1":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "3":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "11":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "6":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "7":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "8":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "9":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "10":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "4":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
    elif user_states[user_id] == Fruit_9:
        if message == "11":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Правельно")
            img10="https://static.wikia.nocookie.net/obedushek/images/f/ff/1986694.jpg/revision/latest?cb=20160611104750&path-prefix=ru"
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=img10)
            text = "\n1 Банан \n2 Апельсин \n3 Яблуко \n4 Абрикос \n5 Мандарин \n6 Папая \n7 Вишня \n11 Виноград \n8 Сливка \n9 Груша \n10 Маракуя"
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
            user_states[user_id] += 1
        elif message == "2":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "1":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "3":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "11":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "6":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "7":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "8":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "9":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "10":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "4":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "5":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
    elif user_states[user_id] == Fruit_10:
        if message == "8":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Правельно")
            img11="https://yesfrukt.com/storage/source/0f494eef36046ddb3223867e02350e99/content/1/xyMiQSxRPe4pojDgSx4f-zxofYyQaUe7f.jpeg.pagespeed.ic.GShY-v5PZe.jpg"
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=img11)
            text = "\n1 Банан \n2 Апельсин \n3 Яблуко \n4 Абрикос \n5 Мандарин \n6 Папая \n7 Вишня \n11 Виноград \n8 Сливка \n9 Груша \n10 Маракуя"
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
            user_states[user_id] += 1
        elif message == "2":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "1":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "3":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "11":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "6":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "7":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "8":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "9":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "10":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "4":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "5":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
    elif user_states[user_id] == Fruit_11:
        if message == "6":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Правельно")
            img12="https://content.rozetka.com.ua/goods/images/original/15464191.png"
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=img12)
            text = "\n1 Банан \n2 Апельсин \n3 Яблуко \n4 Абрикос \n5 Мандарин \n6 Папая \n7 Вишня \n11 Виноград \n8 Сливка \n9 Груша \n10 Маракуя"
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
            user_states[user_id] += 1
        elif message == "2":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "1":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "3":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "11":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "6":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "7":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "8":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "9":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "10":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "4":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "5":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
    elif user_states[user_id] == Fruit_12:
        if message == "10":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Правельно")
            text = "Вітаю ти пройшов гру Вгадай Фрукт."
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
            user_states[user_id] = 1
            text = "Гра закінчилась. Введіть /start, щоб почати знову."
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
        elif message == "2":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "1":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "3":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "11":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "9":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "6":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "4":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "10":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "7":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
        elif message == "5":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неправельно Спобуй Ще раз")
    else:
        pass

start_handler = CommandHandler('start', start_command_handler)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text & ~Filters.command, text_message_handler)
dispatcher.add_handler(echo_handler)

# Start bot
updater.start_polling()
