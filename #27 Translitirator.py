# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 22:13:45 2024

@author: Acer
"""

# 27-DARS TRANSLITIRATOR
from transliterate import to_cyrillic, to_latin
import telebot
TOKEN="6728863016:AAGXbu3IoCdMqy91K2SEKCp1asrgeN9e_bs"
bot = telebot.TeleBot(TOKEN, parse_mode=None)
@bot.message_handler(commands=['start']) # start help komanda-
def send_welcome(message): # siga 👈bu funksiya javob beradi
    javob="Assalomu alaykum, xush kelibsiz."
    javob+="\nMatn kiriting: "
    bot.reply_to(message, javob)
@bot.message_handler(func=lambda m: True) # agar biz matn jo'natsak True
def echo_all(message): # qaytaradi va jo'natgan matndan
    msg=message.text
    javob=lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, javob(msg)) # buni qaytaradi
bot.polling()







# print(to_latin("Дастур")) # Krill alifbodagi matnni lotin alifbosiga o't-
# # kazadi.
# print(to_cyrillic("Assalomu alaykum qandaysiz.")) # Lotin alifbosidagi matnni krill-
# # alifbosiga o'tkazadi.
# matn=input("Matn kiriting:")
# # matn.isascii()  isascii degani birinchi kompyuterlar klaviaturasi faqat
# # lotin alifbosida terilgan. Bu funksiya lotin alifbosida bo'lsa True aks
# # holda False qaytaradi. Bir misol qilamiz.
# if matn.isascii(): # agar matn lotin alifbosida bo'lsa
#     print(to_cyrillic(matn))
# else:
#     print(to_latin(matn))
    
